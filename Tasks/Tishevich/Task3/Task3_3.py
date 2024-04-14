# 3. Write a program that takes a string as input and returns a dictionary with the count of each word in the string.
import re
from collections import Counter


user_string = input("Enter your string data: ")
data_list = re.split(r"[-;,.\s]\s*", user_string)
word_count = dict(Counter(data_list))
print(f"Count of word in string is {word_count}")
