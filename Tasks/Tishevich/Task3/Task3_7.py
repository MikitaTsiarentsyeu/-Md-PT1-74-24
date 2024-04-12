# Write a program that takes a string as input and returns the string with all capital letters converted to lowercase
# and vice versa.
def update_letters_in_string(user_string):
    if sum(map(str.islower, user_string)) != 0:
        update_string = user_string.upper()
    else:
        update_string = user_string.lower()
    return print(update_string)


update_letters_in_string(user_string=input("Enter your data: "))
