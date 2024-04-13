# 2. Write a program that takes a list of numbers as input and returns the sum of all even numbers in the list.
user_string = input("Enter your numbers data with space: ")
generate_list = list(user_string.split(" "))
if "" in generate_list:
    generate_list.remove("")
count = 0
for i in generate_list:
    count += int(i)
print(f"Sum of list numbers is {count}")
