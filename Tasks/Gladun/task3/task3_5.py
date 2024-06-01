user_input = list(input("Please, input random words by space: ").split(" "))

result = []

for i in range(0, len(user_input)):
    if len(user_input[i]) > 5:
        result.append(user_input[i])

print(result)