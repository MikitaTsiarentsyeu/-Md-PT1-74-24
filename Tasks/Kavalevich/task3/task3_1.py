user_str = input("Write a text sentence:\n").lower()

list_vowels = list("aeiouy")
number_vowels = 0
for el in user_str:
    if el in list_vowels:
        number_vowels += 1
print(f"Number of vowels: {number_vowels}.")
