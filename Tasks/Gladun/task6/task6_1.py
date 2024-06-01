user_input = input()

def rev(l):
    reverse = ""
    r = 0
    for i in l:
        r -= 1
        reverse += user_input[r]

    print(reverse)

rev(user_input)