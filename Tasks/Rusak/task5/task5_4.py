def count_lowercase_uppercase(string):
    lower_count = sum(1 for char in string if char.islower())
    upper_count = sum(1 for char in string if char.isupper())
    return lower_count, upper_count
