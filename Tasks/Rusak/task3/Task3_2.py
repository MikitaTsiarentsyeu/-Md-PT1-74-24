def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

num_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
print("Sum of even numbers:", sum_even_numbers(num_list))


