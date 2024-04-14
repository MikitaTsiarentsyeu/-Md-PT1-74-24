#First option

def palindrome_check(a):
    if len(a) <= 1:
        return True
    elif a[0] != a[-1]:
        return False
    else:
        return palindrome_check(a[1:-1])

print(palindrome_check("madam"))  
print(palindrome_check("hello"))  



#Second option

def check_palindrome(a):
    if len(a) <= 1:
        return True
    if a[0] == a[-1]:
        return check_palindrome(a[1:-1])  
    else:
        return False

print(check_palindrome("radar"))  
print(check_palindrome("hello"))  

