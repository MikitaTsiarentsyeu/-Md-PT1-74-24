def reverse_string(strng):
    length = len(strng)
    if length == 0:
        return ''
    else:
        ch = strng[-1]
        return ch + reverse_string(strng[:-1])
