from urllib.request import urlopen
from bs4 import BeautifulSoup

print("Program converts usd to byn (ratio 3.25 on 05.03.2024)")
print("type command online to get ratio from internet")
ratio = 3.25

while True:
    usd = input("Write usd value: ")
    if usd.lower() == "online":
        request_result = urlopen("https://myfin.by/currency/minsk")
        soup = BeautifulSoup(request_result, features="html.parser")
        tag = soup.find_all('span', {'class':'accent'})
        sell = float(tag[0].text)
        usd = input("Write usd value: ")
        print(f"ratio from internet 1 usd = {sell}")
        print("byn =", float(usd) * sell)    
    else:
        print("byn =", float(usd) * ratio)
