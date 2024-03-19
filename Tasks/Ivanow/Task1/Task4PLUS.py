import requests
from bs4 import  BeautifulSoup

page = requests.get('https://myfin.by/currency/minsk?working=0')
soup = BeautifulSoup(page.content, 'html.parser')

currency = float(str(soup.find(class_="accent"))[21:26])

amount_init = float(input('Input money amount: '))
amount_converted = 0
choice = input('Input convert action\n1 - BYN to USD\n2 - USD to BYN\n')

if choice == '1':
    amount_converted = round(amount_init / currency, 2)
    print(f'It will be ${amount_converted}')
elif choice == '2':
    amount_converted = round(amount_init * currency, 2)
    print(f'It will be {amount_converted} BYN')
else:
    print('Error! Unknown input!')
