
while True:
    list_num = list(map(int, input('Enter a list of numbers separated by a space:\n').split()))
    prime_numbers = []
    
    for i in list_num:
        a = 1
        count = 0

        while a <= i//2:
            if i%a==0:
                count +=1
            if count > 1:
                break
            a+=1
        else:
            prime_numbers.append(i)

    print(f'This number {max(prime_numbers)} max prime number in list')