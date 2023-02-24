from enum import Enum


class DataType(Enum):
    grouped = "groupedT"
    single = "t"


data_type = DataType.grouped
topic_num = 10
# File path
data_file_path = './data/' + data_type.value + 'weets.csv'
preprocess_file_path = './result/' + data_type.value + 'weetsTexts.txt'
result_file_path = './result/' + str(topic_num) + 'topic-' + data_type.value + 'weets.html'
stop_word_file_path = "data/stopwordFile.txt"
# IDA model parameter
no_below_threshold = 5
# no_above_threshold is useless
no_above_threshold = 0.8
iteration_num = 400
chunk_size = 1000
pass_num = 10
