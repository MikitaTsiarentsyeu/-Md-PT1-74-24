
while True:
    list_num = list(map(int, input('Enter a list of numbers separated by a space:\n').split()))
    first_max = max(list_num)
    second_max = 0
    for i in list_num:
        if second_max < i and i !=first_max:
            second_max = i
    print(f'Second max number = {second_max}')