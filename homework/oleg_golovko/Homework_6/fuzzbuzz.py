row_numbers = range(1, 101)
fuzz = 'fuzz'
buzz = 'buzz'

for number in row_numbers:
    fuzz_buzz = []
    if number % 15 == 0:
        number = str(number)
        number = number.replace(number, fuzz.title() + buzz.title())
    elif number % 3 == 0:
        number = str(number)
        number = number.replace(number, fuzz)
    elif number % 5 == 0:
        number = str(number)
        number = number.replace(number, buzz)
    fuzz_buzz.append(number)
    print(fuzz_buzz[0])
