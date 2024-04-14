def num_pow(num, n):
    if n == 0:
        return 1
    return num*(num_pow(num, n-1))

print(num_pow(4, 3))