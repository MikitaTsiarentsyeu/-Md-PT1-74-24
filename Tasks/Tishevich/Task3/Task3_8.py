# Write a program that takes a list of numbers as input and returns the average of all numbers in the list.
user_range = int(input("Enter len of numbers list: "))
integer_list = []
for i in range(0, user_range):
    integer_list.append(int(input("Enter your data in integer format: ")))
print(sum(integer_list))
