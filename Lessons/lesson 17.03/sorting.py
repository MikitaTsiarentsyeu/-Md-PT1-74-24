l = [4,6,78,8,5,3,2,3,5,7,9,100]
# l.sort()

# m = sorted(l)
# print(l)
# print(m)

# d = {2:"two", 1:"one"}
# print(sorted(d))

# print(sorted("Test"))

print(l == sorted(l))

# l.sort()

is_sorted = False

# print(is_sorted)

# while not is_sorted:

#     for i in range(len(l)-1):
#         if l[i] > l[i+1]:
#             l[i], l[i+1] = l[i+1], l[i]
    
#     for i in range(len(l)-1):
#         if l[i] > l[i+1]:
#             is_sorted = False
#             break
#     else:
#         is_sorted = True


# print(l)

# counter = 0
# for j in range(len(l)-1):
#     for i in range(len(l)-1-j):
#         counter += 1
#         if l[i] > l[i+1]:
#             l[i], l[i+1] = l[i+1], l[i]

# print(l, counter)

for j in range(len(l)-1):
    min_i = j
    for i in range(min_i+1, len(l)):
        if l[i] < l[min_i]:
            min_i = i
    l[j], l[min_i] = l[min_i], l[j]
    print(l)

