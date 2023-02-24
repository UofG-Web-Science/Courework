import csv


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


def write_text(file_path, texts):
    with open(file_path, 'w') as f:
        for text in texts:
            f.write(str(text) + '\n')


def load_csv(file_path):
    with open(file_path, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
    return reader
