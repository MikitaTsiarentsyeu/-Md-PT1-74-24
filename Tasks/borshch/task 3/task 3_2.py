user_input = list(input("please, enter your numbers separated by commas: \n").split(","))

# solution_1
numbers = []
for i in user_input:
    if int(i) % 2 == 0:
        numbers.append(int(i))
print("the sum of all even numbers in your list is ", sum(numbers))

# solution_2
l = [int(n) for n in user_input if int(n) % 2 == 0]
print("the sum of all even numbers in your list is ", sum(l))
