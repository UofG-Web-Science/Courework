import os

import constant
import data_analyst
import data_preprocessor
import util

if __name__ == '__main__':
    topic_max_num = constant.topic_max_num
    data_param = constant.data_param
    data_type = data_param.data_type
    data_file_path = data_param.data_file_path
    preprocess_file_path = data_param.preprocess_file_path
    no_below_threshold = data_param.no_below_threshold
    no_above_threshold = data_param.no_above_threshold
    iteration_num = data_param.iteration_num
    chunk_size = data_param.chunk_size
    pass_num = data_param.pass_num
    coherence_type = data_param.coherence_type
    # Preprocess data
    if os.path.exists(preprocess_file_path):
        token_texts = []
        lines = util.read_txt(preprocess_file_path)
        for line in lines:
            token_texts.append(eval(line))
    else:
        token_texts = data_preprocessor.process(data_file_path, preprocess_file_path, data_type)
    data_preprocessor.statistical_data(token_texts)
    # Prepare data for modeling
    dic, corpus = data_analyst.vectorise(token_texts, data_type, no_below_threshold, no_above_threshold)
    # Statistical token frequency
    data_analyst.statistical_token_freq(dic)
    # Evaluate topic number
    # data_analyst.evaluate_topic_num(token_texts, dic, corpus, topic_max_num, iteration_num, chunk_size, pass_num,
    #                                 coherence_type, data_type)
    # Modeling topic
    topic_num = data_param.topic_num
    topic_model = data_analyst.modeling_topic(dic, corpus, topic_num, iteration_num, chunk_size, pass_num)
    data_analyst.statistical_topic(topic_model, topic_num, 10)
    topic_model.save('model/lda.model')
    # Evaluate document
    data_analyst.evaluate_doc(topic_model, dic, token_texts)
