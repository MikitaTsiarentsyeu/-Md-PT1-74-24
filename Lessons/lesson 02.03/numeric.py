import decimal
import fractions

number = 12
print(type(number))

number = 999999999999999999999999
print(number)

print(5+85, 45-6, 4*5, 45/5, 45//5)

print(type(45/5))

print(16//3)

number = 4.0

print(3 == 3.0, 3 == 3.000000000000000001)

print(0.1+0.1+0.1 == 0.3)
print(0.1+0.1+0.1)

print(int(4.5555555))
print(float(4))

print(int('123'))
print(float('123.45'))

print(round(3.5))
print(round(4.5))
print(round(5.5))
print(round(6.5))
print(round(7.5))
print(round(8.5))

# x = decimal.Decimal(0.1)
x = decimal.Decimal('0.1')
# print(x+x+0.1)
# print(x/10.0)

x = fractions.Fraction('0.1')
print(x)