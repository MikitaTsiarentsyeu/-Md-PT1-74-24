# while True:
#     print("infinity!")

# x = 5

# while x > 0:
#     print("it's bigger than zero")
# else:
#     print("it's not")

x = 0

while x < 5:
    print(x)
    x += 1
else:
    print("stop!")

l = [1,2,3,4,5]
i = 0
while i < len(l):
    print(l[i])
    i += 1
else:
    print("stop!")


# symbol = 's'

s = "test str"
for symbol in s:
    print(symbol)

print(symbol)

for _ in [1,2,3,4,5]:
    print(_)

print(_)

for i in (1,2,3,4,5):
    print(i)

d = {"one": 1, "two": 2, "three": 3}
for k in d:
    print(k, d[k])

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)

for i in set("test"):
    print(i)

for i in "test":
    print(i)
else:
    print("the end")