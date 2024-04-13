def reverse_str(st):
    if len(st) == 1:
        return st
    else:
        return reverse_str(st[1:]) + st[0]
    
print(reverse_str("The core of extensible programming is defining functions."))
