import random

border_left = int(input('Input left border: '))
border_right = int(input('Input right border: '))

random_num = random.randint(border_left, border_right)
print(f'Generated number: {random_num}')
