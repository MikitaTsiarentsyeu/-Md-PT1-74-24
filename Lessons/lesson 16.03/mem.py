a = 5
b = a

print(a, b)
print(id(a), id(b))

a += 2
# a = a + 2
print(a, b)
print(id(a), id(b))

a = [5]
b = a
print(id(a), id(b))

a[0] += 2
print(a, b)
print(id(a), id(b))

x = 100
y = 100
print(id(x), id(y))
print(id(x) == id(y), x is y)

x = 10000
y = 10000
print(id(x), id(y))
print(id(x) == id(y), x is y)


# s1 = "test test"
# s2 = "test " + "test"
# s3 = input("enter 'test test':")
# print(s1 is s2 is s3)

l = (1,2,3)
m = (1,2,3)
print(l == m, l is m)

l = [1,2,3]
m = [1,2,3]
print(l == m, l is m)