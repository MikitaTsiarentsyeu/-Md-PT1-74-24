# Write a program that calculates the area of a circle given its radius, ask a user for the radius.
import math


user_radius_value = float(input("Enter radius value: "))
s = math.pi * user_radius_value ** 2
print("Area of a circle it's {}".format(round(s, 2)))
