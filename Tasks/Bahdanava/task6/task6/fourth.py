def power(b, e):
    if e == 0:
        return 1
    else:
        return b * power(b, e - 1)

base_num = 2
exponent = 3
result = power(base_num, exponent)
print(f"{base_num} raised to the power of {exponent} is {result}")
