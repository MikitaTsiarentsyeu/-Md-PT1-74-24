import math

print('This program calculates the area of a circle.')

radius = int(input('Enter the radius: '))
while radius <= 0:
    print('The radius must be greater than 0.')
    radius = int(input('Enter the radius: '))

area_cir = math.pi * radius**2
print(f'The area of the circle is {area_cir:.2f}')
