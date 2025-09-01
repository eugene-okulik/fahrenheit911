import random

salary = int(input('Enter your salary: '))

bonus = random.choice([True, False])

if not bonus:
    print(f"{salary}, {bonus} - '${salary}'")
else:
    fin_salary = salary + int(random.random() * salary)
    print(f"{salary}, {bonus} - '${fin_salary}'")
