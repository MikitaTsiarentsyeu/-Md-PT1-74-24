# Write a recursive function to check whether a given string is a palindrome.
def check_palindrome(user_string):
    if len(user_string) < 2:
        return True
    if user_string[0] != user_string[-1]:
        return False
    return check_palindrome(user_string[1:-1])


test_func_result = check_palindrome(user_string=input("Enter your string data: "))
print(test_func_result)
