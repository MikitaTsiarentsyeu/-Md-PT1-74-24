def fibonacci_n_num (n, F_1 = 0, F_2 = 1):  # recursive function to find Nth number in Fibonacci sequence
    if n <= 0:
        raise Exception("searching number should be a positive digit")
    F_n = F_1 + F_2
    if n > 3:
        return fibonacci_n_num(n-1, F_2, F_n)
    elif n == 3:
        return F_n
    elif n == 1:
        return F_1
    else:
        return F_2


print(fibonacci_n_num(8))