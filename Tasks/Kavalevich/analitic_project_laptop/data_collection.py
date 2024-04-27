import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# import pandas as pd        
    
# Получить код html.
def get_response(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response
    except:
        print("Error loading the page", response.status_code)

def find_elem(search_text):
    try:
        target_elem = soup.find(string=search_text).find_parent('td')\
            .find_next_sibling('td').find('span', class_="value__text").text
        return target_elem
    except:
        return ''

# Получить список значений для отзывов (selenium).
def get_list(value):
    value_list = []
    for el in value:
        el = el.text.replace('\n', ' ')
        value_list.append(el)
    return value_list

driver = webdriver.Firefox()

data = []   # Создать список для описания ноутбуков.
lap_num = 1 # Номер ноутбука.
n = 241     # Номер страницы на сайте.

while True:
    print(n)
    url = f"https://catalog.onliner.by/notebook?page={n}"
    driver.get(url)
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'lxml')

    laptops = soup.find_all('div', class_="catalog-form__offers-unit catalog-form__offers-unit_primary")
    for l in laptops:
        #  Получить ссылку на конкретный ноутбук.  
        lap_link = l.find('a', class_="catalog-form__link catalog-form__link_primary-additional "
                    "catalog-form__link_base-additional catalog-form__link_font-weight_"
                    "semibold catalog-form__link_nodecor")['href']    

        # Перейти на страницу одной модели ноутбука.
        response = get_response(lap_link)
        soup = BeautifulSoup(response.text, 'lxml')

        print("lap_num:", lap_num)

        # Получить название ноутбука
        laptom_name = soup.find('h1', class_="catalog-masthead__title js-nav-header").text.strip()
        print(laptom_name)

        # Получить модель процессора.
        search_text = """
                Модель процессора
                                    """
        processor_model = find_elem(search_text)

        # Получить используемую графику.
        search_text = """
                Встроенная в процессор графика
                            """
        graphics = find_elem(search_text)

        # Получить размер экрана.
        search_text = """
                Диагональ экрана
                                    """
        screen_size = find_elem(search_text)          
        
        # Записать характеристики в список.
        laptop_chars = [laptom_name, processor_model, graphics, screen_size]
        
        ratings_list = []
        reviews_list = []
        advantages_list = []
        disadvantages_list = []
        rat_rev_list = []
        
        review_page = 1
        while True:
            print("review_page:", review_page)
            # Получить ссылку для перехода к странице с отзывами. 
            base_review_link = soup.find('div', class_="offers-description__reviews").find_all('a')[0]['href']
            print(base_review_link)

            review_link = base_review_link + f"?page={review_page}"
            print(review_link) 

            if not "create" in review_link:

                # Перейти на страницу с отзывами selenium.
                driver.get(review_link)

                # Получить оценку(текст). 
                ratings = driver.find_elements(By.CLASS_NAME, "offers-reviews__grade-sign")
                ratings_list = get_list(ratings)

                # Получить отзывы.
                reviews = driver.find_elements(By.XPATH, '//*[@id="list"]/div/span')
                reviews_list = get_list(reviews)
                time.sleep(2)

                # Получить достоинства.
                elems = driver.find_elements(By.XPATH, "//*[contains(text(), 'Достоинства:')]")
                for el in elems:
                    advantage = el.find_element(By.XPATH, '..')
                    advantages_list.append(advantage.text)
                    time.sleep(2)

                # Получить недостатки.
                elems = driver.find_elements(By.XPATH, "//*[contains(text(), 'Недостатки:')]")
                for el in elems:
                    disadvantage = el.find_element(By.XPATH, '..')
                    disadvantages_list.append(disadvantage.text) 
                    time.sleep(2)

                # Сохранить оценки с соответствующими отзывами в список.
                for i in range(len(ratings_list)):
                    rev = f"{reviews_list[i]} {advantages_list[i]} {disadvantages_list[i]}"
                    rat_rev_list.append([ratings_list[i], rev])
            else:
                rat_rev_list = ['', '']

            lap_num += 1

            # Добавить все данные об одной модели в список.
            charact = laptop_chars + rat_rev_list
            print(charact)
            data.append(charact)

            # Проверить наличие страниц с отзывами. 
            more_pages = soup.find('a', class_="offers-pagination__main")
            if not more_pages:
                break

            review_page += 1
    
    # Проверить наличие страниц.
    more_pages = soup.find('a', class_="catalog-pagination__main")
    if not more_pages:
        driver.quit()
        break
    n += 1


# print(data)

# https://catalog.onliner.by/notebook?page=1