import math
import decimal
import random


print(math.pi, type(math.pi))

d_pi = decimal.Decimal('3.141592653')
f_pi = 3.14

print(2**3, math.pow(2, 3))
print(144**0.5, math.pow(144, 0.5))

print(math.sqrt(144))

print(math.inf*math.inf)
print(math.nan*9)

print(-math.inf > 99999999999999999)
print(math.nan == 5)

print(math.inf == math.inf)
print(math.nan == math.nan)

print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

# print(3/0) error
print(3/math.inf)