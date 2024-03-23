def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num_list = [int(num) for num in input("Enter a list of numbers separated by spaces: ").split()]
largest_prime = max((num for num in num_list if is_prime(num)), default=None)
if largest_prime is not None:
    print("Largest prime number:", largest_prime)
else:
    print("No prime numbers found.")

