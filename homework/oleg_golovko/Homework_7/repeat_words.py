words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def repeated_words(arg: dict):
    for word, count in arg.items():
        print(word * count)


repeated_words(words)
