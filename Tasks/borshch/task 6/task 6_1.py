string = "any string"
s = list(string)

def reverse_string_recursive(s, l = [], n = None):  #recursive func that returns reversed string
    if n == None:
        n = len(s) - 1
    l.append(s[n])
    if n != 0:
        return reverse_string_recursive(s, l, n-1)
    else:
        return print("".join(str(l).split("', '")).strip("'['").strip("'']"))
