# Func Fibonacci
def func_fibb(num):
    if num <= 1:
        return num
    else:
        return func_fibb(num-1) + func_fibb(num-2)

print(func_fibb(7))