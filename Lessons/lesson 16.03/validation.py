
while True:
    user_input = input("enter your value in format hh:mm\n")

    if len(user_input) != 5:
        print("the input format is incorrect")
        continue

    if user_input[2] != ":":
        print("the input format is incorrect")
        continue

    if user_input.count(':') != 1:
        print("the input format is incorrect")
        continue

    h, m = user_input.split(':')
    print(h, m)

    if not h.isdigit() or not m.isdigit():
        print("the input format is incorrect")
        continue

    h, m = int(h), int(m)

    if h > 24:
        print("the input format is incorrect")
        continue

    break

print("the main logic goes here")