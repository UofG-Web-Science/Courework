import data_analysis
import data_preprocess
import os
import util


if __name__ == '__main__':
    GroupedT = 'groupedT'
    SingleT = 't'
    name = GroupedT
    num_topics = 5

    filePath = './data/' + name + 'weets.csv'
    textStorPath = './result/' + name + 'weetsTexts.txt'
    resultPath = './result/' + str(num_topics) + 'topic-' + name + 'weets.html'
    if os.path.exists(textStorPath):
        texts = []
        lines = util.read_txt(textStorPath)
        for line in lines:
            texts.append(eval(line))
    else:
        texts = data_preprocess.do(filePath, name, textStorPath)
    data_analysis.statistical_data(texts)
    # textPreprocess.textProperty(texts)
    # data_analysis.textAnalyse(texts, num_topics, resultPath)
