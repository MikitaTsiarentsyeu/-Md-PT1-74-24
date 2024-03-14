l = [1,2,3,4,5,"test",[]]
print(l)

print(l[0], l[1], l[2])
l[0] = 0.1
print(l)

# print(str(print))
l = list("test str")
print(len(l), len([]))

print([1,2,3]+[4,5,6])
print([1]*5)

print(l[0], l[1], l[2])
print(l[2:5])
print(l[::-1])

# print(l[5656]) error
# l[8] = "test" error

l.append("new elem")
print(l)

l.extend("new elem")
print(l)

l.insert(0, "new first elem")
print(l)

l.remove('t')
print(l)

print('t' in l)

print(l.pop(), l)
print(l.pop(0), l)

del l[0]
print(l)

del l[3:8]
print(l)

a = 10
l.insert(0, a)
print(l)

del l[0]
print(l)
print(a)

# l.append(l)

# del l
# print(l)

l.clear()
print(l)


print("test" == "rest")
print([1,2,3] == [3,2,1])

l1 = l2 = []
l1.append(1)
print(l2)

l = [1,2,3,4,5]
l[1], l[2] = l[2], l[1]
print(l)