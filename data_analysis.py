import math

from gensim import corpora, models
import matplotlib.pyplot as plt
import pyLDAvis.gensim


def prepModel(texts, num_topics):
    dic = corpora.Dictionary(texts)
    dic.filter_extremes(no_below=10, no_above=0.8)
    corpus = [dic.doc2bow(text) for text in texts]
    # activate dic
    temp = dic[0]
    lda = models.LdaModel(corpus=corpus, id2word=dic.id2token, num_topics=num_topics, iterations=400, chunksize=2262,
                          passes=40)
    topic_list = lda.print_topics(num_topics=num_topics, num_words=10)
    for topic in topic_list:
        print(topic)
    return corpus, dic, lda


def perplexity(num_topics, corpus, dic):
    ldaModel = models.LdaModel(corpus, num_topics=num_topics, id2word=dic, passes=30)
    print(ldaModel.print_topics(num_topics=num_topics, num_words=15))
    print(ldaModel.log_perplexity(corpus))
    return ldaModel.log_perplexity(corpus)


def perplex(corpus, dic, num_topics):
    x = range(1, num_topics+1)
    y = [perplexity(i, corpus, dic) for i in x]

    plt.plot(x, y)
    plt.xlabel('topic num')
    plt.ylabel('coherence')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.title('topic-perplexity')
    plt.show()


def textAnalyse(texts, num_topics, resultPath):
    corpus, dic, lda = prepModel(texts, num_topics)
    # perplex(corpus, dic, num_topics)

    data = pyLDAvis.gensim.prepare(lda, corpus, dic)
    pyLDAvis.save_html(data, resultPath)


def statistical_data(token_texts):
    min_len = math.inf
    max_len = 0
    total_len = 0
    total_len_with_less_10_token = 0

    for token_text in token_texts:
        text_len = len(token_text)
        if text_len > max_len:
            max_len = text_len
        if text_len < min_len:
            min_len = text_len
        if text_len < 10:
            total_len_with_less_10_token += 1
        total_len += text_len
    ave_len = (float(total_len) / len(token_texts))

    print("Total length: ", len(token_texts))
    print("Max length: ", max_len)
    print("Min length: ", min_len)
    print("Average length: ", ave_len)
    print("Total length of text with less than 10 tokens: ", total_len_with_less_10_token)
