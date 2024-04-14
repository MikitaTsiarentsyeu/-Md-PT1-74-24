def count_char(st, ch, count=0):
    if len(st) < 1:
        return count
    else:
        if st[0] == ch:
            count += 1
        return count_char(st[1:], ch, count)
    
string = "The core of extensible programming is defining functions."
char = 't'

print(count_char(string.lower(), char))
