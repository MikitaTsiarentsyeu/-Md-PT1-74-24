formula = input('Input your expression: ')

brackets_count = 0

for i in formula:
    if i == '(':
        brackets_count += 1
    elif i == ')':
        brackets_count -= 1
    if brackets_count <= -1:
        print('Wrong expression!')
        break

if brackets_count % 2:
    print('Your expression missing bracket!')
else:
    print('Everything is great!')
