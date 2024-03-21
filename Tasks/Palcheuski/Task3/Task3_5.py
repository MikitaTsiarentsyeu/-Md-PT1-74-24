
while True:
    user_line = input('Enter a line in English:\n').split()
    string_more_5 = [i for i in user_line if len(i) > 5]
    print(f'String of more than 5 characters\n {string_more_5}')