numbers = input("Enter the numbers separated by commas:\n").split(',')

numb_list = []
for el in numbers:
    numb_list.append(int(el))
av = sum(numb_list) / len(numb_list)
print(f"The average value: {av:.1f}")
