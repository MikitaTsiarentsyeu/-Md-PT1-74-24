user_input = list(input("input random numbers separated by spase: ").split(" "))



for j in range(len(user_input)-1):
    for i in range(len(user_input) - 1 - j):
        if int(user_input[i]) > int(user_input[i + 1]):
            user_input[i] , user_input[i + 1] = user_input[i + 1] , user_input[i]

print(user_input)
print(user_input[1])