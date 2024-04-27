# Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.
def reverse_list_values(user_list_range):
    user_list = []
    for i in range(0, user_list_range):
        user_list.append((input("Enter your data:"))[::-1])
    print(user_list)


reverse_list_values(user_list_range=int(input("Enter list range:")))
