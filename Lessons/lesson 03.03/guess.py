import random

my_number = random.randint(1, 10)
your_number = int(input("Guess an integer number from 1 to 10: "))

if my_number == your_number:
    print("Lucky guess!")
else:
    print("Loser!")