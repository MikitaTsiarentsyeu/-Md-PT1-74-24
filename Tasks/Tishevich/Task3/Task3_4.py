# 4. Write a program that takes a list of numbers as input and returns the second largest number in the list.
user_string = input("Enter your numbers data with space: ")
generate_list = list(user_string.split(" "))
new_list = []
for i in generate_list:
    new_list.append(int(i))
second_larges_value = (sorted(new_list))[-2]
print(f"Second largest number in list is {second_larges_value}")
