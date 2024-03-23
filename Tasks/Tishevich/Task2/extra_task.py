# напиши программку, которая подсчитает вхождение каждой буквы в определённой строке (допустим пользователь вводит)
# давай пройдёмся по классике - напиши программку, которая подсчитает вхождение каждой буквы в определённой строке
# (допустим пользователь вводит)
from collections import Counter


def string_checker(user_string):
    string_count = Counter(user_string)
    return print(dict(string_count))


string_checker(user_string=input("Enter your string data: "))
