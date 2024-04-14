# func reverse

def func_reverse(text:str):
    if len(text) == 0:
        return text
    else:
        return text[-1] + func_reverse(text[:-1])
    

print(func_reverse(input('Enter a line:\n')))