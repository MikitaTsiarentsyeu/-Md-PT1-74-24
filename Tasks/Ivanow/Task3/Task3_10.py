nums = list(input('Input your numbers:\n'))

numbers = ''
num = 0

for i in nums:
    not_prime = False
    if int(i) == 2:
        numbers += i
    if int(i) > 1:
        for num in range(2, int(i)):
            if int(i) % num == 0:
                not_prime = True
                break
            if not not_prime:
                numbers += i
                break

for i in numbers:
    if int(i) > num:
        num = int(i)

print(num)