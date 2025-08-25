raw_text = '''Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,
facilisisv itae semper at, dignissim vitae libero'''

suffix = 'ing'

raw_words = raw_text.split()
words_with_suffix = []

for word in raw_words:
    if word.endswith(','):
        words_with_suffix.append(word[:-1] + suffix + ',')
    elif word.endswith('.'):
        words_with_suffix.append(word[:-1] + suffix + '.')
    else:
        words_with_suffix.append(word + suffix)

fin_text = ' '.join(words_with_suffix)
print(fin_text)
