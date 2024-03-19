l = [x for x in range(10)]
print(l, list(range(10)))

l = [str(x) for x in range(10)]
print(l)

# l = []
# for x in range(10):
#     l.append(str(x))

s = {str(x) for x in range(10)}
print(s)

d = {x:str(x) for x in range(10)}
print(d)

# t = (str(x) for x in range(10))
# print(t)
# print(list(t))


l = [x*x for x in range(100) if x % 2 == 0]
print(l)


l = [str(x*x) if x % 2 == 0 else '' for x in range(100) ]
print(l)

l = [x*x for x in range(100) if x % 2 == 0 if len(str(x)) == 2 and x > 30 ]
print(l)

# l = []
# for x in range(100):
#     if x % 2 == 0:
#         if len(str(x)) == 2 and x > 30:
#             l.append(x*x)

numbers = [1,2,3,4,5]
letters = "abc"
l = [f"{num}{letter}" for num in numbers for letter in letters]
print(l)

# l = []
# for num in numbers:
#     for letter in letters:
#         l.append(f"{num}{letter}")

l = [[1,2,3], [4,5,6], [7,8,9]]

# res = []
# for i in l:
#     for j in i:
#         res.append(j)
# print(res)

print([j for i in l for j in i])