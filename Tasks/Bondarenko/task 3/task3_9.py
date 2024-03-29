example = "Good Morning!"
result = ""

#solution 1
print(example[::-1])

#solution 2
print("".join([str(i) for i in reversed(list(example))]))

#solution 3
for i in reversed(list(example)):
    result += i

print(result)