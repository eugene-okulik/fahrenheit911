my_dict = {
    'tuple': (1, 3, 6, 7, None, 'text', False, 2.42),
    'list': [1, 3, 6, 7, None, 'text', False, 2.42, 'sdsdf', 'last', 'last2'],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {1, 3, 6, 7, None, 'text', False, 2.42},
}

print(my_dict['tuple'][-1])
my_dict['list'].append('last3')
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = 6
my_dict['dict'].pop('a')
my_dict['set'].add('python')
my_dict['set'].remove(1)
print(my_dict)
