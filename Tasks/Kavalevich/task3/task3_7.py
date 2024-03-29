user_str = input("Write a text sentence:\n")

new_list = []
for el in user_str:
    if el.islower():
        new_list.append((el.upper()))
    elif el.isupper():
        new_list.append(el.lower())
    else:
        new_list.append(el)
new_string = ''.join(new_list)
print(new_string)
