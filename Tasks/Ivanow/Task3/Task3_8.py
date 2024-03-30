nums = list(input())

summ = 0
aver = 0

for i in nums:
    summ += int(i)

aver = int(summ / len(nums))

print(aver)