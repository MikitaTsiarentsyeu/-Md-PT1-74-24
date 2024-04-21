# Write a recursive function to reverse a string.
def reversing_string(user_string):
    if user_string == "":
        return ""
    return reversing_string(user_string[1:]) + user_string[0]


check_result = reversing_string(user_string=input("Enter your data: "))
print(check_result)
