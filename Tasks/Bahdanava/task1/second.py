import math

def circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

radius = float(input("Enter the radius: "))
circle = circle_area(radius)
rounded_circle = round(circle, 2)
print("The circle area is:", rounded_circle)




import math

def circle_area(radius):
     area = math.pi * (radius ** 2)
     return area

while True:
    radius = input("Enter the radius (or type 'end' to exit): ")
    if radius.lower() == 'end':
        break
    radius = float(radius)
    circle = circle_area(radius)
    rounded_circle = round(circle, 2)
    print("The circle area is: ", rounded_circle)

