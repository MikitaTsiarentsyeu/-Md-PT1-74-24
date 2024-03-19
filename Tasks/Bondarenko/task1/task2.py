import math
print("Program calculates area of circle by radius")
while True:
    radius = float(input("Write radius value: "))
    print("Area =", format(math.pi * radius**2, ".4f"))
