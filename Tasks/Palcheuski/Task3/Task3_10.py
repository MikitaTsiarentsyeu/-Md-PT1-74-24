
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
            if i == 0 or i == 1:
                continue 
            prime_numbers.append(i)

    if len(prime_numbers)!=0:
        print(f'This number {max(prime_numbers)} max prime number in list')
    else:
        print('There are no prime numbers')