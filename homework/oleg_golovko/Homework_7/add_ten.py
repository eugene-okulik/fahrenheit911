text = 'результат работы программы: 209'


def add_ten(line):
    parts = line.split()
    number = int(parts[-1])
    return number + 10


print(add_ten(text))
