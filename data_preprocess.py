import csv
import math
import string
import util
import os

stop_word_file_path = "data/stopwordFile.txt"


def do(file_path, name, output_path):
    texts = read_data(file_path, name)
    token_texts = integrate_data(texts)
    util.write_text(output_path, token_texts)

    return token_texts


def read_data(file_path, data_type):
    rows = util.read_csv(file_path)
    match data_type:
        case "t":
            texts = []
            for i, row in enumerate(rows):
                # Skip the header
                if i == 0:
                    continue
                if float(row[3]) < 0.45 or float(row[4]) < 0:
                    continue
                texts.append(row[2])
        case "groupedT":
            grouped_texts = {}
            for i, row in enumerate(rows):
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


def integrate_data(texts):
    token_texts = []
    # Load stop words
    stop_words = util.read_txt(stop_word_file_path)
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
        token_texts.append(tokens)

    return token_texts


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
