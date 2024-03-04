a = float(input("Enter the rational 'a' value: "))
b = float(input("Enter the rational 'b' value: "))
c = float(input("Enter the rational 'c' value: "))

D = b*b - 4*a*c

if D > 0:
    b1 = (-b + D**0.5)/(2*a)
    b2 = (-b - D**0.5)/(2*a)
    print(b1, b2)
elif D == 0:
    b = -b/(2*a)
    print(b)
else:
    print("no roots")