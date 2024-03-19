f = 'fizz'
b = 'buzz'

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f+b)
#     elif i % 5 == 0:
#         print(b)
#     elif i % 3 == 0:
#         print(f)
#     else:
#         print(i)

# for i in range(1, 101):
#     r = ""
#     if i % 3 == 0:
#         r += f
#     if i % 5 == 0:
#         r += b
#     if not r:
#         r = i
#     print(r)

l = [("fizz"*(i%3==0) + "buzz"*(i%5==0)) or i for i in range(1, 101)]
print(l)