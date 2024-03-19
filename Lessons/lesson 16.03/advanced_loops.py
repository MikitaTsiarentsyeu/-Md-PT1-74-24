# while True:
#     pass

s = "test str"
i = 0
is_break = False
while True:
    if i == len(s):
        is_break = True
        break
    print(s[i])
    i += 1
else:
    print("the end?")


for i in [1,2,3,4,5,6,7,8]:
    if i == 6:
        break
    if i % 2 == 0:
        continue
    print(i)
else:
    print("the end?")


