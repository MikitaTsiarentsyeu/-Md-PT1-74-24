def count_ch(ch, string, count=0):
    length = len(string)
    if length == 0:
        return count
    if ch == string[0]:
        count += 1
    return count_ch(ch, string[1::], count)
