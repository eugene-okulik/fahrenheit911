my_list = []
num1 = int(input('Enter first number: '))
my_list.append(num1)
num2 = int(input('Enter second number: '))
my_list.append(num2)

num1, num2 = my_list


def mathematical_operation(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            return func(first, second, operation='*')
        elif first == second:
            return func(first, second, operation='+')
        elif first > second:
            return func(first, second, operation='-')
        else:
            return func(first, second, operation='/')

    return wrapper


@mathematical_operation
def calc(first, second, operation):
    print(operation)
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    else:
        raise ValueError("Unknown operation")


print(calc(num1, num2))
