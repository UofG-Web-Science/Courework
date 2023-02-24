import os

import constant
import data_analysis
import data_preprocess
import util

if __name__ == '__main__':
    topic_num = constant.topic_num
    data_type = constant.data_type
    data_file_path = constant.data_file_path
    preprocess_file_path = constant.preprocess_file_path
    result_file_path = constant.result_file_path
    # Preprocess data
    if os.path.exists(preprocess_file_path):
        token_texts = []
        lines = util.read_txt(preprocess_file_path)
        for line in lines:
            token_texts.append(eval(line))
    else:
        token_texts = data_preprocess.do(data_file_path, data_type, preprocess_file_path)
    data_preprocess.statistical_data(token_texts)
    # Statistical token frequency
    # dic, corpus = data_analysis.convert_text(token_texts)
    # data_analysis.statistical_token_freq(dic)
    # Calculate perplexity
    # data_analysis.statistical_perplexity(dic, corpus, topic_num)
    # Visualize result
    # Modeling topic
    topic_model, corpus, dic = data_analysis.do(token_texts, topic_num)
    data_analysis.statistical_topic(topic_model, topic_num, 15)
    data_analysis.statistical_perplexity(dic, corpus, topic_num)
    data_analysis.visualize_result(topic_model, corpus, dic, result_file_path)
