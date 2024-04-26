def reverse_string_recursive(string):

    if len(string) <= 1:
        return string
    else:
        return reverse_string_recursive(string[1:]) + string[0]
