# 5. Write a program that takes a list of strings as input and returns a list with all strings that have a length
# greater than 5 characters.
data_list = []
for i in range(3):
    user_string = input("Enter your numbers data with space: ")
    if len(user_string) > 5:
        data_list.append(user_string)

print(f"String list with string(-s) more then 5 character is {data_list}")
