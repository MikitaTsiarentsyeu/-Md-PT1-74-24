import random

my_number = random.randint(0, 10)

while True:
    your_number = int(input("Guess the number from 1 to 10: "))

    if your_number == my_number:
        print("Congratulations!")
        break
    else:
        print("Try again")




import random

my_number = random.randint(0, 10)
your_number = int(input("Guess the number from 1 to 10: "))

if my_number == your_number:
    print("Congratulations!")
else:
    print("Try again")


