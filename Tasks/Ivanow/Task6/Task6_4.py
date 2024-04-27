
def calc_power(num, p):
    if p == 1:
        return num
    if p == 0:
        return 1
    p -= 1
    return num * calc_power(num, p)
