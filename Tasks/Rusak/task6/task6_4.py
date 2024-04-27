def power_recursive(base, exponent):
    if exponent == 0:
        return 1
    return base * power_recursive(base, exponent - 1)
