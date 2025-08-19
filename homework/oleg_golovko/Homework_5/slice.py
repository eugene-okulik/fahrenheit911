text = "результат операции: 42"
colon_index = text.index(":")
result = int(text[colon_index + 2 :])
print(result + 10)
