
while True:
    list_num = list(map(int, input('Enter a list of numbers separated by a space:\n').split()))
    result = sum(list_num) / len(list_num)
    print(f'result = {result}')