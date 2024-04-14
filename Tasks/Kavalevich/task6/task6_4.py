def calculate_power(numb, power):
    if power == 0:
        return 1
    elif power > 0:
        return numb * calculate_power(numb, power-1)
    else:
        return 1/calculate_power(numb, -power)

print(calculate_power(5, 4))
