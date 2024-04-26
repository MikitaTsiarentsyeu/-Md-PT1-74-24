# Write a function that takes an ordered list of numbers without duplicates and returns a string
# with ranges for those numbers, check the example below:
# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"
import itertools


def get_ranges(numbers_list):
    data = (list(number) for i, number in
            itertools.groupby(numbers_list, lambda number, data_count=itertools.count(): number - next(data_count)))
    return print(', '.join('-'.join(map(str, (item[0], item[-1])[:len(item)])) for item in data))


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])
