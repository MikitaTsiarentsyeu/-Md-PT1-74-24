l = ["two", "chair", "plate"]


def reversed_str(l):  # returns list of reversed strings from list
    new_l = []
    for i in l:
        m = list(i)
        i = m[::-1]
        new_l.append("".join(str(i).split("', '")).strip("'['").strip("'']"))
    print(new_l)
