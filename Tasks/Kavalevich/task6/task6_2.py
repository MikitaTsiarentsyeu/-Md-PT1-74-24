def is_palindrome(st):
    if len(st) < 1:
        return True
    else:
        if st[0] == st[-1]:
            return is_palindrome(st[1:-1])
        else:
            return False
        
print(is_palindrome("asdffdsa"))
print(is_palindrome("asfdsa"))
