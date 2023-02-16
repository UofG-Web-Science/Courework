import csv
import test

from gensim import corpora , models
import matplotlib.pyplot as plt


column = []
with open('groupedTweets.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i == 0:
            continue
        column.append(row[3])


texts = test.calc_representation(column)
print(texts)

# with open ('texts2.txt','w') as f:
#      f.write(str(texts))

# min_length = -1
# max_length = 0
# sum_length = 0
# average_length = 0


# for text in texts:
#     length = len(text)
#     if length > max_length:
#           max_length = length
#     if length < min_length or min_length == -1:
#         min_length = length
#     sum_length += length
# average_length = (float(sum_length)/ len(texts))

          
# print(max_length)
# print(min_length)
# print(average_length)


dic = corpora.Dictionary(texts)
dic.filter_extremes(no_below=10, no_above=0.8)
corpus = [dic.doc2bow(text) for text in texts]   



# lda = models.LdaModel(corpus=corpus, id2word=dic, num_topics=2, passes = 30,random_state=1)
# topic_list=lda.print_topics(num_topics=3, num_words=10)
# print(topic_list)


# import pyLDAvis.gensim

# data = pyLDAvis.gensim.prepare(lda, corpus, dic)
# pyLDAvis.save_html(data, '2topic-group.html')

# def perplexity(num_topics):
#     ldamodel = models.LdaModel(corpus, num_topics=num_topics, id2word = dic, passes=30)
#     print(ldamodel.print_topics(num_topics=num_topics, num_words=15))
#     print(ldamodel.log_perplexity(corpus))
#     return ldamodel.log_perplexity(corpus)




# x = range(1,5)
# z = [perplexity(i) for i in x]  #如果想用困惑度就选这个

# plt.plot(x, z)
# plt.xlabel('主题数目')
# plt.ylabel('coherence大小')
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus']=False
# plt.title('主题-perplexity变化情况')
# plt.show()


num_topics = 2
temp = dic[0]
lda = models.LdaModel(corpus=corpus, id2word=dic.id2token, num_topics=num_topics, iterations=400, chunksize=2262, passes=40)
topic_list = lda.print_topics(2)
for topic in topic_list:
    print(topic)



file_test = texts[1:20]
corpus_test = [dic.doc2bow(text) for text in file_test]
topics_test = lda.get_document_topics(corpus_test)


labels = ['UK','London','Glasgow']
for i in range(3):
    print('这条'+labels[i]+'新闻的主题分布为：\n')
    # list[ 主题ID，相关概率 ]s
    print(topics_test[i],'\n')

    id_list =[]
    pro_list=[]
    
    for l in topics_test[i]:
        #print(l)
        id_list.append(l[0]+1)
        pro_list.append(l[1])
        
    plt.figure(figsize=(10,4),dpi=80)
    plt.title(labels[i])
    plt.bar(id_list, pro_list)
    
    plt.xlabel(u'topic')
    plt.ylabel(u'relatively')
    
    plt.xlim(0.5, num_topics+0.5)
    plt.ylim(0.0, max(pro_list)+0.1)
    plt.show()
    
    topic_id=id_list[pro_list.index(max(pro_list))]
    print(str(topic_id)+"号主题:相关性"+str(max(pro_list)))





