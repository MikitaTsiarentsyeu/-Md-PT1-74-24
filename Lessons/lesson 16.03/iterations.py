for i in range(10):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(1, 11, 2):
    print(i)

s = "tttssssjkljkjjjjjj"
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        continue
    print(s[i])


x = range(10000)
print(x)
print(list(x))

for index, value in enumerate(s):
    if index < len(s)-1:
        if value == s[index+1]:
            continue
    print(value)


l = [1,2,3,4,5]
# for i in l:
#     print(i)

it = iter(l)
# print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#print(next(it))
