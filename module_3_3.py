def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


list = ['l1', 'l2', 'l3']
string = 'str'
dict = {'a': 1, 'b': 2, 'c': 3}
print_params()
print_params(1, 2, 3)
print_params(*list)
print_params(*string)
print_params(**dict)
print_params(b = 25) #работает
print_params(c = [1, 2, 3]) #работает

values_list = [1, 'two', [3,4]]
values_dict = {'a': 11, 'b': 2.2, 'c': 'd' }
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [(1,2,3), 'wdfga']
print_params(*values_list_2, 42)

