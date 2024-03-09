a = input('Input value or "?" to find: ')
b = input('Input value or "?" to find: ')
c = input('Input value or "?" to find: ')

answer = 0

if a == '?':
    b, c = float(b), float(c)
    if b > c:
        print('error! catheter > hypotenuse')
        exit()
    else:
        answer = (c * c - b * b) ** 0.5
elif b == '?':
    a, c = float(a), float(c)
    if a > c:
        print('error! catheter > hypotenuse')
        exit()
    else:
        answer = (c * c - a * a) ** 0.5
elif c == '?':
    a, b = float(a), float(b)
    answer = (a * a + b * b) ** 0.5
else:
    print('Incorrect input/not enough values')

print(round(answer, 2))
