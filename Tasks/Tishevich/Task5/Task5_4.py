# Write a function that takes a string as an argument and returns two numbers, first for count of lower
# case letters, second for count of the upper case letters in the initial string.
def check_hight_letters_in_string(user_string):
    lower_letter = sum(map(str.islower, user_string))
    upper_letter = sum(map(str.isupper, user_string))
    return print(f"Sum of lower case letter is {lower_letter}, sum of upper case letter is {upper_letter}")


check_hight_letters_in_string(user_string=input("Enter your data: "))
