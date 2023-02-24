import text_analysis
import data_preprocess
import os
import util


if __name__ == '__main__':
    GroupedT = 'groupedT'
    SingleT = 't'
    name = GroupedT
    num_topics = 5

    filePath = 'data/' + name + 'weets.csv'
    preprocess_output_path = 'result/' + name + 'weetsTexts.txt'
    resultPath = 'result/' + str(num_topics) + 'topic-' + name + 'weets.html'

    if os.path.exists(preprocess_output_path):
        # Read list from file
        lines = util.read_txt(preprocess_output_path)
        texts = []
        for line in lines:
            texts.append(eval(line))
    else:
        texts = data_preprocess.do(filePath, name, preprocess_output_path)
    # textPreprocess.textProperty(texts)
    text_analysis.textAnalyse(texts, num_topics, resultPath)
