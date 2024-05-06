l = int(input("enter first count: "))
m = int(input("enter second count: "))

def power(l , m):
    if m == 0:
        return 1
    else:
        return l * (power(l , m - 1))

print(power(l , m))