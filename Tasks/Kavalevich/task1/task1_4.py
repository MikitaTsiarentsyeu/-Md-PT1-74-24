from urllib.request import urlopen
from bs4 import BeautifulSoup

# The first version.
CONVERSION = 3.2300

print('This program converts some amount of money from USD to BYN.')
print('The first version.')


def get_amount_byn(converting):
    print(f'The exchange rate is {converting:.4f}')
    amount_dollars = int(input('Enter the amount of dollars you want to exchange: '))
    while amount_dollars <= 0:
        print('The amount cannot be less than or equal to 0.')
        amount_dollars = int(input('Enter the amount of dollars you want to exchange: '))
    amount_byn = amount_dollars * converting
    return amount_byn


print(f'You will get {get_amount_byn(CONVERSION):.2f} BYN.')
print()

# The second version.
print('The second version.')

request_result = urlopen('https://kurs.onliner.by/')
soup = BeautifulSoup(request_result, features='html.parser')
tag_list = soup.find_all('p', {'class': 'value'})
buy_doll_text = tag_list[0].text
split_string = buy_doll_text.split()[0].replace(',', '.')
online_conversion = float(split_string)

print(f'You will get {get_amount_byn(online_conversion):.2f} BYN.')
