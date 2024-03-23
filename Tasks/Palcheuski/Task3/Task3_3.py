
while True:
    user_line = input('Enter a line in English:\n').split()
    dic_line = {}
    for i in user_line:
        if i in dic_line:
            dic_line[i] += 1
        else:
            dic_line[i] = 1
    print(f'Dictionary with the number of each word {dic_line}')
