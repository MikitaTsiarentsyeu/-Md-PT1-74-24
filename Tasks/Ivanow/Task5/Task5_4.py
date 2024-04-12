
def count_case(s):
    count_lower = 0
    count_upper = 0
    for c in s:
        if c == c.lower():
            count_lower += 1
        elif c == c.upper():
            count_upper += 1
        else:
            continue
    return count_lower, count_upper
