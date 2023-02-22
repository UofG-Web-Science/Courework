import csv
import string


def load_txt(file_path):
    lines = []
    with open(file_path, 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            # Remove blank space
            if '\n' == line:
                continue
            # Remove line break
            line = line.strip('\n')
            lines.append(line)

    return lines


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
    stop_words = load_txt(stop_word_file_path)
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


def textStor(filePath, texts):
    with open(filePath, 'w') as f:
        f.write(str(texts))


def textPreProcess(filePath, name, textStorPath):
    try:
        with open(textStorPath, 'r', encoding="utf-8") as f:
            texts = eval((f.readlines())[0])
        return texts
    except IOError:
        GroupedT = 'groupedT'
        SingleT = 't'
        column = []
        with open(filePath, 'r', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                if name == SingleT:
                    column.append(row[2])
                elif name == GroupedT:
                    column.append(row[3])
        texts = calc_representation(column)
        textStor(textStorPath, texts)
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
