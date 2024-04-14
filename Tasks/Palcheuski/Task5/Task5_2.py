# Function reverse
def func_reverse(list_st:list):
    return [list_reverse[::-1] for list_reverse in list_st]

st_list = input('Enter a list of strings: ').split()
new_list = func_reverse(st_list)
print(new_list)