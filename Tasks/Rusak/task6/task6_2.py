def is_palindrome_recursive(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return is_palindrome_recursive(string[1:-1])
    else:
        return False
