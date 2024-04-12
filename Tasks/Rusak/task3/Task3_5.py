def filter_long_strings(string_list):
    return [string for string in string_list if len(string) > 5]

string_list = input("Enter a list of strings separated by spaces: ").split()
filtered_strings = filter_long_strings(string_list)
print("Strings with length greater than 5 characters:", filtered_strings)
