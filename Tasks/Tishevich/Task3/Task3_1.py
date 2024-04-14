#  1. Write a program that takes a string as input from a user and returns the number of vowels in the string.
cirillic_vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
latinic_vowels = ["a", "e", "i", "o", "u", "y"]
user_string = input("Enter your data: ")
vowels_count = {}
for i in user_string:
    if i in latinic_vowels:
        vowels_count[i] = user_string.count(i)
    if i in cirillic_vowels:
        vowels_count[i] = user_string.count(i)
print(f"Count vowels in string is {vowels_count}")
