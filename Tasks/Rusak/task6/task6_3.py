def count_occurrences_recursive(string, char):
    if len(string) == 0:
        return 0
    if string[0] == char:
        return 1 + count_occurrences_recursive(string[1:], char)
    else:
        return count_occurrences_recursive(string[1:], char)
