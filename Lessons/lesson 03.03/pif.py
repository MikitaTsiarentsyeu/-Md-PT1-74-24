a = input("Enter the rational 'a' value or '?' to find a value:")
b = input("Enter the rational 'b' value or '?' to find a value:")
c = input("Enter the rational 'c' value or '?' to find a value:")

count = (a == '?') + (b == '?') + (c == '?')
# if a == '?':
#     count += 1
# if b == '?':
#     count += 1
# if c == '?':
#     count += 1
if count != 1:
    print("incorrect unknown values count, should be only one")
    exit()


if c == '?':
    a = float(a)
    b = float(b)

    res = (a*a + b*b)**0.5
elif a == '?':
    c = float(c)
    b = float(b)

    res = (c*c - b*b)**0.5
else:
    c = float(c)
    a = float(a)

    res = (c*c - a*a)**0.5


print(res)

# print(a, b, c)
# print(a, b, c, sep='   ')