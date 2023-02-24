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
