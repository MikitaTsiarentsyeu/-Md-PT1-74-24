list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

prime_numb = []
for numb in list_numbers:
    if numb < 2:
        pass
    else:
        for i in range(2, int(numb**0.5) + 1):
            if numb % i == 0:
                break
        else:
            prime_numb.append(numb)
print(prime_numb)
print(f'The largest prime number in the list: {max(prime_numb)}')
