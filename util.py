import csv


def read_txt(file_path):
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


def write_text(file_path, lines):
    with open(file_path, 'w') as f:
        for line in lines:
            f.write(str(line) + '\n')


def read_csv(file_path):
    rows = []
    with open(file_path, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
    return rows
