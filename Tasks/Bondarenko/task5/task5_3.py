def getstr_list(func_list):
    return [i for i in func_list if len(i) > 5]

list = ["hello world", "function", "visual studio code", "file", "code"]
print(getstr_list(list))