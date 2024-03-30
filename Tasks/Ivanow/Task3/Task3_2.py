nums = list(input('Input your numbers:\n'))

sum = 0

for i in nums:
    if not(int(i) % 2):
        sum += int(i)
    else:
        continue

print(f'Even numbers sum = {sum}')