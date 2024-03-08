import random

print('This program generates a random number in a given range.')
begin = int(input('Enter the left border: '))
end = int(input('Enter the right border: '))
while begin > end:
    print('The right border cannot be smaller than the left border.')
    end = int(input('Enter the right border: '))

rand_numb = random.randint(begin, end)
print(f'The random number is {rand_numb}.')
