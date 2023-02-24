import matplotlib.pyplot as plt
import pyLDAvis.gensim
from gensim import corpora, models

import constant

no_below_threshold = constant.no_below_threshold
no_above_threshold = constant.no_above_threshold
iteration_num = constant.iteration_num
chunk_size = constant.chunk_size
pass_num = constant.pass_num


def do(token_texts, topic_num):
    dic, corpus = convert_text(token_texts)
    topic_model = modeling_topic(dic, corpus, topic_num)

    return topic_model, corpus, dic


def modeling_topic(dic, corpus, topic_num):
    topic_model = models.LdaModel(corpus=corpus, id2word=dic.id2token, num_topics=topic_num, iterations=iteration_num,
                                  chunksize=chunk_size,
                                  passes=pass_num)

    return topic_model


def convert_text(token_texts):
    dic = corpora.Dictionary(token_texts)
    # Filter out words with too low frequency or too high frequency
    dic.filter_extremes(no_below=no_below_threshold, no_above=no_above_threshold)
    corpus = [dic.doc2bow(text) for text in token_texts]
    # activate dic
    temp = dic[0]
    return dic, corpus


def statistical_topic(lda_model, topic_num, word_num):
    topics = lda_model.show_topics(num_topics=topic_num, num_words=word_num, formatted=False)
    for topic in topics:
        print(topic)


def statistical_perplexity(dic, corpus, topic_num):
    perplexity = []
    for i in range(1, topic_num + 1):
        lda_model = modeling_topic(dic, corpus, i)
        perplexity.append(lda_model.log_perplexity(corpus))

    x = range(1, topic_num + 1)
    plt.plot(x, perplexity)
    plt.xlabel('Topic Number')
    plt.ylabel('Perplexity')
    plt.show()


def statistical_token_freq(dic):
    token_freq = sorted(dic.cfs.items(), key=lambda x: x[1], reverse=False)
    for (token_id, num) in token_freq:
        print(dic.get(token_id), num)


def visualize_result(topic_model, corpus, dic, result_file_path):
    data = pyLDAvis.gensim.prepare(topic_model, corpus, dic)
    pyLDAvis.save_html(data, result_file_path)
