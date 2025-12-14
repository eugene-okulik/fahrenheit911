def repeat_me(func):
    def wrapper(*args, count=1):
        i = 0
        while i < count:
            func(*args)
            i += 1

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
