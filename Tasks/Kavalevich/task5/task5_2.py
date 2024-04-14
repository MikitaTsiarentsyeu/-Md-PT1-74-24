def reversed_list(some_list):
    new_list = [el[::-1] for el in some_list]
    return new_list

my_list = ['this', 'is', 'my', 'list']

print(reversed_list(my_list))
