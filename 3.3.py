def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b='ari')
print_params(a=2, c=False)
print_params(a=3, b='eternity', c=False)
print_params(b=25)
print_params(c = [1,2,3])

values_list = ['music', 8, 'cat']
values_dict ={'a': 7, 'b' : 'horse', 'c' : [5,8,8]}
print_params(*values_list)
print_params(**values_dict)

values_list_2=[5,'fish']
print_params(*values_list_2, 42)