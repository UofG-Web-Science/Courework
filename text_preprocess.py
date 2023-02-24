import csv
import string
import util
import os

def clean_text(text):
    for ch in text:
        if f"'{ch}'" == ascii(ch):
            pass
        else:
            text = text.replace(ch, " ")
    # Remove blank break
    text = text.replace('\n', " ")
    return text


def clean_token(token, stop_words):
    # Remove NULL
    if len(token) == 0:
        return ''
    # Exclude #, @, $
    if token.startswith('#') or token.startswith('@') or token.startswith('$'):
        token = token.replace(":", "")
        token = token.replace(".", "")
        token = token.replace(",", "")
        return token
    # Remove URL
    if token.startswith('http') or token.startswith('&amp'):
        return ''
    # Remove punctuation
    exclude = set(string.punctuation)
    token = ''.join(ch for ch in token if ch not in exclude)
    # Remove stop words
    if token.lower() in stop_words:
        return ''
    return token


def calc_representation(texts):
    # Load stop words
    stop_word_file_path = "./data/stopwordFile.txt"
    stop_words = util.load_txt(stop_word_file_path)
    tokenList = []
    for text in texts:
        # Clean text
        text = clean_text(text)
        # Split text into tokens
        raw_tokens = text.split(" ")
        tokens = []
        # Clean tokens
        for raw_token in raw_tokens:
            token = clean_token(raw_token, stop_words)
            if len(token) != 0:
                tokens.append(token)
        tokenList.append(tokens)
    return tokenList


def textPreProcess(file_path, name, output_path):
    if os.path.exists(output_path):
        # TODO Load list from file
        texts = util.load_txt(output_path)
        return texts

    texts = load_data(file_path, name)
    texts = calc_representation(texts)
    util.write_text(output_path, texts)

    return texts


def load_data(file_path, data_type):
    with open(file_path, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        match data_type:
            case "t":
                texts = []
                for i, row in enumerate(reader):
                    # Skip the header
                    if i == 0:
                        continue
                    if float(row[3]) < 0.45 or float(row[4]) < 0:
                        continue
                    texts.append(row[2])
            case "groupedT":
                grouped_texts = {}
                for i, row in enumerate(reader):
                    # Skip the header
                    if i == 0:
                        continue
                    # Skip low quality text by qSocre < 0.45 or nScore < 0
                    if float(row[4]) < 0.45 or float(row[5]) < 0:
                        continue
                    group_id = row[0]
                    grouped_text = grouped_texts.get(group_id, "")
                    grouped_text = grouped_text + " " + row[3]
                    grouped_texts[group_id] = grouped_text
                texts = list(grouped_texts.values())

    return texts


def textProperty(texts):
    min_length = -1
    max_length = 0
    sum_length = 0
    threshold_sum_10 = 0

    for text in texts:
        length = len(text)
        if length > max_length:
            max_length = length
        if length < min_length or min_length == -1:
            min_length = length
        if length < 10:
            threshold_sum_10 += 1
        sum_length += length
    average_length = (float(sum_length) / len(texts))
    print("Total tweets num: ", len(texts))
    print("MAX length: ", max_length)
    print("MIN length: ", min_length)
    print("AVG length: ", average_length)
    print("Total tweets num(shorter than 10 words): ", threshold_sum_10)
