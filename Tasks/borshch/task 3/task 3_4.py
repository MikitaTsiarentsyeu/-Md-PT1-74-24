numbers = [1, 5, 65, 587, 148, 367, 9654, 225, 2, 96, 47, 5, 7, 3]

for i in range(len(numbers) - 1):
    for k in range(i+1, len(numbers)):
        if numbers[k] < numbers[i]:
            numbers[i], numbers[k] = numbers[k], numbers[i]

print("the second largest number in this list is ", numbers[-2])
