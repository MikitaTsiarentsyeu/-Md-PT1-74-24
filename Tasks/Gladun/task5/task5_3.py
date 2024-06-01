user_input = list(input("enter the string by space: ").split())

def len5(user_input):
    s5 = []
    for i in user_input:
        if len(i) > 5:
            s5.append(i)

    print(s5)

len5(user_input)