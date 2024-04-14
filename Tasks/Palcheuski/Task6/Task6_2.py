# Func palindrome

def func_palindr(text):
    flag = True
    if len(text) > 1:
        if text[0] == text[-1]:
            return func_palindr(text[1:-1])
        else:
            flag = False
            return flag
    else:
        return flag

print(func_palindr('Enter the world:\n'))
