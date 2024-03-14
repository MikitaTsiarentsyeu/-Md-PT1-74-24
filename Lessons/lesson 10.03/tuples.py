t = (1,2,3,4,5,"test",[])
print(t, type(t), len(t))

t = ()
print(t, type(t), len(t))

t = (1,)
print(t, type(t), len(t))

t = (1,2,3,4,5,"test",[])
print(t[0], t[-1], t[:3])

print((1,2,3)+(4,5,6), (0,)*3)

print(t.index(3))

t = list(t)
t.append("new elem")
t = tuple(t)
print(t)

l = [1,2,3]
m = [1,2,3]
print(l == m, l is m)
l.append(1)
print(l, m)

l = (1,2,3)
m = (1,2,3)
print(l == m, l is m)