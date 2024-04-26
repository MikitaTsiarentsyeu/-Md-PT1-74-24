def palindrome(string):
    length = len(string)
    if length == 0:
        return 'is palindrome'
    ch_f = string[0]
    ch_l = string[-1]
    if ch_f == ch_l:
        return palindrome(string[1:-1])
    else:
        return 'not palindrome'
