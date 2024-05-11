immutable_var=(1, 2, False, 'Привет', 5.3)
print('immutable_var: ', immutable_var)
# immutable_var[2]=True - данная операция невозможна, поскольку кортеж является неизменяеммы списком!
mutable_list=[5, 'А это элемент списка!', 2.4, True]
mutable_list[1]='Этот элемент изменен!'
print('mutable_list: ', mutable_list)