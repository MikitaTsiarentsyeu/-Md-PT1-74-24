l = list('abc')
print(l)

print('a' in l)
print('a' in 'abc')

l = ['abc', 'def', 'ghi']
print('abc' in l)
print('a' in l)

target = 'test'
res = False
for string in l:
    print(string)
    if target in string:
        res = True
        break
print(res)

l = [list('abc'), list('def'), list('ghi'), list('test')]
print(l)


target = 'e'
res = False
for i in range(len(l)):
    # is_stop = False
    # print(l[i])
    for j in range(len(l[i])):
        # print(l[i][j])
        if l[i][j] == target:
            res = (i, j)
            # is_stop = True
            break
    if res != False:
        break
print(res)