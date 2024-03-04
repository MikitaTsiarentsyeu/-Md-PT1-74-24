import math

circle_radius = float(input('Input circle radius: '))

PI = math.pi
circle_area = round( PI * circle_radius ** 2, 1)

print(f'Circle area = {circle_area}')