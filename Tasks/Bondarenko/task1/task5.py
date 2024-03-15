import random
print("Program generate number in user range")
while True:
    left = int(input("Write left border: "))
    right = int(input("Write right border: "))
    print(f"Random number between {left} and {right} = ",random.randint(left, right))
