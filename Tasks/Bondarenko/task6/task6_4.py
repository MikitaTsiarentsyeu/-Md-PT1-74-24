
def power(base, exponent) -> int:
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1) 

print(power(2,8))
print(power(3,3))