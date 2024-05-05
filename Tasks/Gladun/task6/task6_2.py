l = input()

def rev(l):
    if len(l) < 2:
        return "it's palindrom"
    elif l[0] != l[-1]:
        return "it isn't palindrom"
    return rev(l[1:-2])

rev(l)

print(rev(l))