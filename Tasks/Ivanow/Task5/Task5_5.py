def get_ranges(l):

    ranges = ''
    range_start = l[0]
    range_end = l[0]

    for num in l[1:]:
        if num == range_end + 1:
            range_end = num
        else:
            if range_start == range_end:
                ranges += str(range_start)
            else:
                ranges += f"{range_start}-{range_end}, "
            range_start, range_end = num, num

    # Add the last range
    if range_start == range_end:
        ranges += str(range_start)
    else:
        ranges += f"{range_start}-{range_end}"

    return ranges