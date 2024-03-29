#First option

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

#Second option

def is_prime(number_):
    largest_prime = None
    for number in number_:
        if number > 1:
            is_prime = True
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                if largest_prime is None or number > largest_prime:
                    largest_prime = number
    return largest_prime

num = [10, 5, 4, 14, 53, 197, 46, 26, 73, 3, 1, 97]
largest_prime = is_prime(num)
if largest_prime is not None:
    print("The largest prime number:", largest_prime)
else:
    print("No prime numbers found in the list.")
