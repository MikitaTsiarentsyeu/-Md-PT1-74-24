# Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.

def generate_list_from_string_with_five_or_more_symbol(user_list_range):
    user_list = []
    for i in range(0, user_list_range):
        value_for_strings_list = input("Enter your data:")
        if len(value_for_strings_list) > 4:
            user_list.append(value_for_strings_list)
    print(user_list)


generate_list_from_string_with_five_or_more_symbol(user_list_range=int(input("Enter list range:")))
