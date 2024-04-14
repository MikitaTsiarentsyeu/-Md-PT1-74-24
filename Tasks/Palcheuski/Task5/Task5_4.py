# Func (upper or lower) case letters
def fun_upp_or_low(user_string):
    count_lower = 0
    count_upper = 0
    for i in user_string:
        if i >= 'a' and i <= 'z':
            count_lower += 1
        elif i >= 'A' and i <= 'Z':
            count_upper += 1
    return print(f"Lowercase letters = {count_lower}\nUppercase letters = {count_upper}")


fun_upp_or_low(input('Enter the line:\n'))
