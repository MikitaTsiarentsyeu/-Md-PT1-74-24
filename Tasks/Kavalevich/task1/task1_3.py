print('This program converts kilometers per hour to meters per second.')
kilometers_hour = int(input('Enter the speed (km/h): '))
while kilometers_hour < 0:
    print('The speed cannot be less than 0.')
    kilometers_hour = int(input('Enter the speed (km/h): '))

meters_second = kilometers_hour * 0.278
print(f'The speed is {meters_second:.0f} meters per second')
