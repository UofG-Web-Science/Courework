import text_analysis
import text_preprocess


if __name__ == '__main__':
    GroupedT = 'groupedT'
    SingleT = 't'
    name = GroupedT
    num_topics = 5

    filePath = './data/' + name + 'weets.csv'
    textStorPath = './results/' + name + 'weetsTexts.txt'
    resultPath = './results/' + str(num_topics) + 'topic-' + name + 'weets.html'

    texts = text_preprocess.textPreProcess(filePath, name, textStorPath)
    # textPreprocess.textProperty(texts)
    text_analysis.textAnalyse(texts, num_topics, resultPath)
