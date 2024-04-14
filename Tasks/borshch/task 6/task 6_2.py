any_string = "weather is great"
ads = "1010101"


def palindrome_func(any_string, low = 0, high = None):  # this function checks string as palindrome
    if high == None:
        high = len(any_string) - 1
    if any_string[low] == any_string[high]:
        if low == high and len(any_string) != 1 or high == low+1:
            return print("this is palindrome")
        elif len(any_string) == 1:
            raise Exception("string should be longer than 1 symbol")
        else:
            return palindrome_func(any_string, low + 1, high - 1)
    else:
        return print("this string isn't palindrome")

palindrome_func(ads)
