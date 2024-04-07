l = ["two", "chair", "plate"]


def reversed_str(l):
    new_l = []
    for i in l:
        
        l[i] = list(l[i]) , -1]
        new_l.append(l[i])
    print(new_l)

print(reversed_str(l))
