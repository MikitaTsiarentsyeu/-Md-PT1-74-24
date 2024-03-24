with open("data.txt", 'r') as f:
    data = f.read()

print(repr(data))

obj = eval(data)
print(obj, type(obj))

print(obj[0][0])

# eval is evil

