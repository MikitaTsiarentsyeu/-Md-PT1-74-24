user_input = input("please enter list of your numbers separated with comma")

l = user_input.replace(" ", "").split(",")
m = {}
for i in l:
    if not i.isdigit():
        raise Exception ("please enter only numbers")
    i = int(i)
    for j in range(1, i + 1):
        if i % j == 0:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1

prime_numbers = []
for keys, values in m.items():
    if values == 2:
        prime_numbers.append(keys)

print(max(prime_numbers))




