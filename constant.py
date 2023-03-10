from enum import Enum


class DataParam:
    def __init__(self, data_type, data_file_path, no_below_threshold, no_above_threshold, iteration_num, chunk_size,
                 pass_num, coherence_type, topic_num):
        self.topic_num = topic_num
        self.coherence_type = coherence_type
        self.pass_num = pass_num
        self.chunk_size = chunk_size
        self.iteration_num = iteration_num
        self.no_above_threshold = no_above_threshold
        self.no_below_threshold = no_below_threshold
        self.preprocess_file_path = './result/' + data_type.name + "_tweets-preprocessed.txt"
        self.data_type = data_type
        self.data_file_path = data_file_path


class DataType(Enum):
    grouped = "groupedT"
    single = "t"


stop_word_file_path = "data/stopwordFile.txt"

topic_max_num = 8

topic_distribution_threshold = 0.5
single_param = DataParam(DataType.single, "data/tweets.csv", 10, 0.1, 400, 100, 20, 'c_uci', 4)
group_param = DataParam(DataType.grouped, "data/groupedTweets.csv", 5, 0.4, 400, 460, 20, 'c_v', 4)

data_param = single_param
