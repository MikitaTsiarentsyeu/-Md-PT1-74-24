eq = input("enter yore len eq in a format y=kx+b:\n")
x = int(input("enter the x value:\n"))

eq = eq.replace(' ', '').replace('y=', '')
print(eq)
k, b = eq.split('x')

k = int(k)
b = int(b)
y = k*x+b
print(y)