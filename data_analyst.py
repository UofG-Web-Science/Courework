import matplotlib.pyplot as plt
import pyLDAvis.gensim
from gensim import corpora, models

import constant


def convert_text(token_texts, data_type, no_below_threshold, no_above_threshold):
    dic = corpora.Dictionary(token_texts)
    # Filter out words with too low frequency or too high frequency
    dic.filter_extremes(no_below=no_below_threshold, no_above=no_above_threshold)
    corpus = [dic.doc2bow(text) for text in token_texts]
    match data_type:
        case constant.DataType.single:
            corpus = models.tfidfmodel.TfidfModel(corpus)[corpus]
        case constant.DataType.grouped:
            pass
    # activate dic
    temp = dic[0]

    return dic, corpus


def modeling_topic(dic, corpus, topic_num, iteration_num, chunk_size, pass_num):
    topic_model = models.LdaModel(corpus=corpus, id2word=dic.id2token, num_topics=topic_num, iterations=iteration_num,
                                  chunksize=chunk_size,
                                  passes=pass_num)

    return topic_model


def statistical_token_freq(dic):
    token_freq = sorted(dic.cfs.items(), key=lambda x: x[1], reverse=False)
    for (token_id, num) in token_freq:
        print(dic.get(token_id), num)


def evaluate_topic_num(token_texts, dic, corpus, topic_max_num, iteration_num, chunk_size, pass_num, coherence_type,
                       data_type):
    coherence_scores = []
    perplexity_scores = []
    idxs = range(1, topic_max_num + 1)
    for i in idxs:
        topic_model = modeling_topic(dic, corpus, i, iteration_num, chunk_size, pass_num)
        coherence = statistical_coherence(topic_model, token_texts, dic, corpus, coherence_type)
        coherence_scores.append(coherence)
        perplexity = statistical_perplexity(topic_model, corpus)
        perplexity_scores.append(perplexity)
        visualize_topic(topic_model, corpus, dic, data_type)
    # Visualize evaluation
    x = idxs
    plt.plot(x, coherence_scores)
    plt.xlabel('Topic Number')
    plt.ylabel(coherence_type + ' Coherence')
    plt.title(data_type.name + ' ' + coherence_type + ' Coherence')
    plt.savefig('result/' + data_type.name + '-coherence.svg')
    plt.show()
    plt.plot(x, perplexity_scores)
    plt.xlabel('Topic Number')
    plt.ylabel('Perplexity')
    plt.title(data_type.name + ' Perplexity')
    plt.savefig('result/' + data_type.name + '-perplexity.svg')
    plt.show()


def statistical_coherence(topic_model, token_texts, dic, corpus, coherence_type):
    coherence_model = models.CoherenceModel(model=topic_model, texts=token_texts, corpus=corpus, dictionary=dic,
                                            coherence=coherence_type, processes=8)
    coherence = coherence_model.get_coherence()

    return coherence


def statistical_perplexity(topic_model, corpus):
    perplexity = (topic_model.log_perplexity(corpus))

    return perplexity


def visualize_topic(topic_model, corpus, dic, data_type):
    # Skip if only one topic
    if topic_model.num_topics == 1:
        return
    data = pyLDAvis.gensim.prepare(topic_model, corpus, dic)
    result_file_path = './result/' + data_type.name + '-' + str(topic_model.num_topics) + '.html'
    pyLDAvis.save_html(data, result_file_path)


def statistical_topic(topic_model, topic_num, word_num):
    topics = topic_model.show_topics(num_topics=topic_num, num_words=word_num, formatted=False)
    for topic in topics:
        print(topic)
