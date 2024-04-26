# Write a recursive function to calculate the power of a given number.
def power_by_user_number(number, number_for_power):
    if number_for_power == 0:
        return 1
    else:
        return number * power_by_user_number(number, number_for_power-1)


test_func = power_by_user_number(number=float(input("Enter your number: ")),
                                 number_for_power=int(input("Enter the exponent of number: ")))
print(test_func)
