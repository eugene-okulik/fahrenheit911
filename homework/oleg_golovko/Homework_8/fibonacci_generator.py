def fibonacci(a, b):
    while True:
        yield a
        a, b = b, a + b


count = 0
for x in fibonacci(0, 1):
    count += 1
    if count == 5:
        print(x)
        continue
    elif count == 200:
        print(x)
        continue
    elif count == 1000:
        print(x)
        continue
    elif count == 100000:
        print(x)
        break
