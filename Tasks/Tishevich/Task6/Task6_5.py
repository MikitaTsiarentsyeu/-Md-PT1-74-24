# Write a recursive function to find the Nth number in the Fibonacci sequence.
def find_fibonacci_number(number):
    if number <= 1:
        return number
    return find_fibonacci_number(number - 1) + find_fibonacci_number(number - 2)


test_func = find_fibonacci_number(number=int(input("Enter your number: ")))
print(test_func)
