#5. Write a function that takes an ordered list of numbers without duplicates and returns a string with ranges for those numbers, check the example below:

def get_ranges(numbers):
    if not numbers:
        return ""

    ranges = []
    start = end = numbers[0]

    for num in numbers[1:]:
        if num == end + 1:
            end = num
        else:
            if start == end:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}-{end}")
            start = end = num

    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}-{end}")

    return ', '.join(ranges)

print(f'"{get_ranges([0, 1, 2, 3, 4, 7, 8, 10])}"',  
      f'"{get_ranges([4, 7, 10])}"',                
      f'"{get_ranges([2, 3, 8, 9])}"',
      sep="; ")