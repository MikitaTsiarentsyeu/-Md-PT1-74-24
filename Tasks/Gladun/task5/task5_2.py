user_input = list(input("enter the string by space: ").split())
def rev(user_input):
    l = list()
    for i in user_input:
        m = list(i)
        i = m[::-1]
        l.append(''.join(str(i).split("', '")).strip("'['").strip("']'"))
    print(l)

rev(user_input)

# one two three