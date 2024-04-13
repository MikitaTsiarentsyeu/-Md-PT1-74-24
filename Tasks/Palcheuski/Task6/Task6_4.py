# Func power

def func_power(num, p):
    if p > 1:
        return num * func_power(num, p - 1)
    else:
        return num


print(func_power(2,5))