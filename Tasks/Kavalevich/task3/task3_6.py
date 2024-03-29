user_str = input("Write a text sentence:\n").lower()

list_vowels = list("aeiouy")

new_list = []
for el in user_str:
    if el not in list_vowels:
        new_list.append(el)
new_string = ''.join(new_list).capitalize()
print(new_string)
