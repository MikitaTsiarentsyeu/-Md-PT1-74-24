strings = ["wave", "mountain", "high", "eleven", "refrigerator", "window"]

# solution 1
res = []

for i in range(len(strings)):
    if len(strings[i]) > 5:
        res.append(strings[i])

print(res)

# solution 2
l = [x for x in strings if len(x) > 5]

print(l)
