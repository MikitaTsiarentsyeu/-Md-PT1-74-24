user_input = input("enter the string: ")

user_input = user_input.split(" ")
d = {}
i = 0

for i in user_input:
    if i in d:
        d[i] = d[i] + 1
        continue
    d[i] = 1

print(d)