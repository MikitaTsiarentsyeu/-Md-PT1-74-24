def revers_list(func_list):
    return [i[::-1] for i in func_list]

list = ["hello world", "function", "visual studio code"]
print(revers_list(list))