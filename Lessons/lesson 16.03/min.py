l = [3,5,5,3,2,23,4,6,8,9,7,0]

# print(sorted(l)[0])

# print(min(l))

min_i = 0
for i in range(1, len(l)):
    if l[i] < l[min_i]:
        min_i = i
print(min_i, l[min_i])

target = 2
target_i = False
for i in range(len(l)):
    if l[i] == target:
        target_i = i
        break
print(target_i)