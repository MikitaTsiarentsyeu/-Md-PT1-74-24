

def check_ocurences(string, char) -> int:
    if not string:
        return 0
    elif string[0] == char:
        return 1 + check_ocurences(string[1:], char)
    else:
        return check_ocurences(string[1:], char)

print(check_ocurences("hello world", "o"))
print(check_ocurences("hellooooooo world", "o"))

