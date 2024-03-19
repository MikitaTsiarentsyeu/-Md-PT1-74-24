numbers_l = [1, 5, 7, 3, 2, 6, 4]
num_t = 11
numbers_t = []
numbers_q = [1, 5, 7, 3, 2, 6, 4]

for i in range(len(numbers_l) // 2 + 1):
    num1 = numbers_l[i]
    num2 = numbers_l[(-i-1)]
    if num1 + num2 == num_t:
        numbers_t.append(num1)
        numbers_t.append(num2)

print(numbers_t)

