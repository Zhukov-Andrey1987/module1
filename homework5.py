print('Part one:') # Для обозначения частей задания
my_list = ['Банан', 'Яблоко', 'Ананас', 'Груша', 'Киви', 'Персик']
print('List:', my_list)
print('First element: ', my_list[0])
print('Last element: ', my_list[-1])
print('Sublist: ', my_list[2:5])
my_list[2] = 'Апельсин'
print('Modified list: ', my_list)

# Далее работа со словарем

print('Part two:')
my_dict = {'Банан': 'Banana','Яблоко': 'Apple', 'Ананас': 'Pineapple', 'Груша': 'Pear'}
print('Dictionary: ', my_dict)
print('Word translation "Ананас": ', my_dict['Ананас'])
my_dict['Киви'] = 'Kiwi' # Решил добавить, а не изменять значение, чтобы не портить смысл словаря! :)
print('Modified dictionary:', my_dict)