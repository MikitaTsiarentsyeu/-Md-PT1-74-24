def second_largest(numbers):
    unique_numbers = sorted(set(numbers), reverse=True)
    if len(unique_numbers) < 2:
        return "There is no second largest number."
    return unique_numbers[1]

num_list = [int(num) for num in input("Enter a list of numbers separated by spaces: ").split()]
print("Second largest number:", second_largest(num_list))
