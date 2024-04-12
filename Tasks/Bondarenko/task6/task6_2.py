def check_polindrome(string) -> bool:
    if len(string) < 2:
        return True
    if string[0] != string[-1]:
        return False
    return check_polindrome(string[1:-1])

string = "hello"
print(check_polindrome(string))
string = "noon"
print(check_polindrome(string))
string = "tacocat"
print(check_polindrome(string))