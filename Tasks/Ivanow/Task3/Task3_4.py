nums = list(input('Enter numbers:\n'))

temp = 0
max = 0

for i in nums:
    if int(i) > max:
        max = int(i)

for i in nums:
    if max > int(i) > temp:
        temp = int(i)

print(f'Second largest number: {temp}')