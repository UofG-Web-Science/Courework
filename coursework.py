import textAnalyse
import textPreprocess


if __name__ == '__main__':
    GroupedT = 'groupedT'
    SingleT = 't'
    name = SingleT
    num_topics = 10

    filePath = './data/' + name + 'weets.csv'
    textStorPath = './results/' + name + 'weetsTexts.txt'
    resultPath = './results/' + str(num_topics) + 'topic-' + name + 'weets.html'

    texts = textPreprocess.textPreProcess(filePath, name, textStorPath)
    textPreprocess.textProperty(texts)
    # textAnalyse.textAnalyse(texts, num_topics, resultPath)
