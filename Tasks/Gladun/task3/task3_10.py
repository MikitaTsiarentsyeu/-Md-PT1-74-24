l = list(input("Please, input a random numbers by space: ").split())

result = []

for i in range(0 , len(l)):
    if int(l[i]) == 2 or int(l[i]) == 3 or int(l[i]) == 5:
        result.append(l[i])
    elif int(l[i]) > 1 and int(l[i]) != 0:
        if int(l[i]) % 2 == 0:
            continue
        elif int(l[i]) % 3 == 0:
            continue
        elif int(l[i]) % 5 == 0:
            continue
        else:
            result.append(l[i])

print(result)
print(max(result))

# 1 2 3 4 5 6 7 8 9 10 0 11 12 50 100 97 23 56