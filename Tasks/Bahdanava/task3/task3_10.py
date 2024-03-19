def is_prime(number_):
    res_ = []
    for number in number_:
        if number > 1:
            res = []
            for i in range(2, int(number - 1)):
                res.append(number % i)
            if not 0 in res:
                res_.append(number)
    return sorted(res_)[-1]


num = [10, 5, 4, 14, 53, 197, 46, 26, 73, 3, 1, 97]
print("The largest prime number: ", is_prime(num))