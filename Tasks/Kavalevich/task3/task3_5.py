list_str = input("write words or sentences without using"
                 " punctuation marks:\n").split(' ')

new_list = []
# new_list = [new_list.append(el) for el in list_str if len(el) > 5]
for el in list_str:
    if len(el) > 5:
        new_list.append(el)
print(new_list)
