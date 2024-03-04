
amount_BYN = float(input('Input your BYN amount: '))

currency = 3.26

amount_USD = round(amount_BYN / 3.26, 2)
print(f'It will be {amount_USD}$')