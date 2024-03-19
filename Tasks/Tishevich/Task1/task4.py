# Write a program that converts some amount of money from USD to BYN, ask a user for the amount, store the ratio inside
# the program itself.
import requests
from bs4 import BeautifulSoup


usd_count = float(input("Enter USD amount: "))
page = requests.get("https://kurs.onliner.by/")
soup = BeautifulSoup(page.text, "html.parser")
usd_currency = float((((soup.find_all('p', {'class': 'value'}))[2]).text[:-4]).replace(',', '.'))
billing_data = float('{:.2f}'.format(usd_count * usd_currency))
print(f"Count of BYN by NB-RB: {billing_data}")
