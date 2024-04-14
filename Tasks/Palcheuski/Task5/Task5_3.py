# Function str>5
def func_list_with_str_more_than_5(list_st:list):
    return [str_i for str_i in list_st if len(str_i)>5]

st_list = input('Enter a list of strings: ').split()
new_list_with_str_more_than_5 = func_list_with_str_more_than_5(st_list)
print(new_list_with_str_more_than_5)