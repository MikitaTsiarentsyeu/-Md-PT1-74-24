from urllib.request import urlopen
from bs4 import BeautifulSoup

request_result = urlopen("https://kurs.onliner.by/")
# print(request_result)
soup = BeautifulSoup(request_result, features="html.parser")
tag_list = soup.find_all('p', {'class':'value'})

buy = tag_list[0].text
sell = tag_list[1].text

print(buy, sell)