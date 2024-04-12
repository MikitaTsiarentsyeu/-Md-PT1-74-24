num_list = [float(num) for num in input("Enter a list of numbers separated by spaces: ").split()]
average = sum(num_list) / len(num_list) if num_list else "List is empty."
print("Average:", average)
