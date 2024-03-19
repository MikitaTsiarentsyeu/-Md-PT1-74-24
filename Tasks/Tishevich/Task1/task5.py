# Write a program that generates a random number in a given range, and shows the answer to a user, ask a user for
# the left and right border.
from random import randint

user_left_value_border = int(input("Enter left border value: "))
user_right_value_border = int(input("Enter right border value: "))
random_value = randint(user_left_value_border, user_right_value_border)
print(f"Random number in given range is {random_value}")
