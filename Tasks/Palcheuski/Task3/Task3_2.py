
while True:
    list_num = list(map(int, input('Enter a list of numbers separated by a space:\n').split()))
    even_sum = 0
    for n in list_num:
        if n % 2 == 0:
            even_sum += n
    print(f'The sum of all even numbers = {even_sum}')