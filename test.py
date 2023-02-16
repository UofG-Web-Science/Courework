import jieba, re
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
    stop_word_file_path = "../tweets/stopwordFile.txt"
    stop_words = load_txt(stop_word_file_path)
    tokenlist = []
    for text in (texts):
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
        tokenlist.append(tokens)
    return tokenlist
    



# # 去除原始字符串中的url
# def remove_urls(raw_sentence):
#     # 正则表达式
#     url_reg = r'[a-z]*[:.]+\S+'
#     result = re.sub(url_reg, '', raw_sentence)
#     return result


# # 去除原始字符串中的emoji字符
# def remove_emoji(raw_sentence):
#     for ch in raw_sentence:
#         if f"'{ch}'" == ascii(ch):
#             pass
#         else:
#             raw_sentence = raw_sentence.replace(ch, " ")
#     # Remove blank break
#     raw_sentence = raw_sentence.replace('\n', " ")
#     return raw_sentence




# # 利用jieba分词对文档进行中文分词
# def seg_depart(raw_sentence):

#     if len(raw_sentence) == 0:
#         return None
#     # Exclude #, @, $
#     if raw_sentence.startswith('#') or raw_sentence.startswith('@') or raw_sentence.startswith('$'):
#         raw_sentence = raw_sentence.replace(":", "")
#         raw_sentence = raw_sentence.replace(".", "")
#         raw_sentence = raw_sentence.replace(",", "")
#         return raw_sentence
    
#     # Remove punctuation
#     exclude = set(string.punctuation)
#     raw_sentence = ''.join(ch for ch in raw_sentence if ch not in exclude)

#     sentence_depart = jieba.cut(raw_sentence.strip())
#     outstr = ''
#     for word in sentence_depart:
#         if word not in stopwordslist:
#             outstr += word
#             outstr += " "
#     return outstr







# def final_remove(result):
#     pre_sentence_1 = remove_urls(result)
#     pre_sentence_2 = remove_emoji(pre_sentence_1)
#     final_sentence = seg_depart(pre_sentence_2)
#     return final_sentence



