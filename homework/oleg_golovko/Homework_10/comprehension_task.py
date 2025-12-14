PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = PRICE_LIST.split()

data = [tuple(new_list[i:i + 2]) for i in range(0, len(new_list), 2)]

my_dict = {key: int(value[:-1]) for key, value in data}

print(my_dict)
