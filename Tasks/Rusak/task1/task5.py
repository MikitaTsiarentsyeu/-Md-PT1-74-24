import random

left_border = int(input("Enter the left border of the range: "))
right_border = int(input("Enter the right border of the range: "))

random_number = random.randint(left_border, right_border)
print(f"The random number in the range [{left_border}, {right_border}] is: {random_number}")
