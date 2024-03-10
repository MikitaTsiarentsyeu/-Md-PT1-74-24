# print(hash("test"))

d = {1:"one", 2:"two", "three":3}
print(d, type(d), len(d))

print(d[1], d["three"])

print(d)
d["new key"] = "new value"
print(d, d["new key"])

# d["test"] error

d["new key"] = "test"
print(d)

d = {1:"one", 2:"two", "three":3, 1: 1.0}
print(d)

print(1 in d, "two" in d.values())
print(list(d))
print(list(d.values()))
print(list(d.items()))

print(d.get("one", False))

del d[1]
print(d)