l = [0, 1, 2, 3, 4, 7, 8, 10]
q = [4,7,10]
w = [2, 3, 8, 9]

def get_ranges(l):  # returns ranges from the list
    m = []
    n = []
    for i in range(len(l)):
        if i == len(l)-1:
            n.append(l[i])
            m.append(n)
        elif l[i+1] - l[i] == 1:
            n.append(l[i])
        else:
            n.append(l[i])
            m.append(n)
            n = []
    my_range = ""
    for j in range(len(m)):
        if m[j][0] == m[j][-1]:
            if j == len(m) - 1:
                my_range += f"{m[j][0]}"
            else:
                my_range += f"{m[j][0]}" + ", "
        elif j == len(m) - 1:
            my_range += f"{m[j][0]}-{m[j][-1]}"
        else:
            my_range += f"{m[j][0]}-{m[j][-1]}" + ", "
    return print(my_range)

get_ranges(w)
