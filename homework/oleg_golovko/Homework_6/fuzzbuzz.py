row_numbers = range(1, 101)
fuzz = 'fuzz'
buzz = 'buzz'

for number in row_numbers:
    if number % 15 == 0:
        number = fuzz.title() + buzz.title()
    elif number % 3 == 0:
        number = fuzz
    elif number % 5 == 0:
        number = buzz
    print(number)
