import datetime

initial_date = "Jan 15, 2023 - 12:05:33"

python_date = datetime.datetime.strptime(initial_date, '%b %d, %Y - %X')

month_from_date = python_date.strftime('%B')

new_date = python_date.strftime('%d.%m.%Y, %H:%M')

print(python_date)
print(month_from_date)
print(new_date)
