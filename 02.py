def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(12, c=False)
print_params(b=[1, 2, 3], a='str', c=dict())
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['a', 2, [1, 2, 3]]
values_dict = {'a': 2, 'b': [1, 2, 3], 'c': ['1', 2, 3]}

print_params(**values_dict)
print_params(*values_list)
# print_params(*values_list, **values_dict)

values_list_2 = ['a', 2]
print_params(*values_list_2, 42)