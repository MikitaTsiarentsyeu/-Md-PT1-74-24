user_input_string = input("please, enter your string")

punctuation_marks = [".", ",", "?", "!", ";", ":", "(", ")", "'", "-"]

for i in user_input_string:
    if i in punctuation_marks:
        user_input_string = user_input_string.replace(i, " ")

list_of_words = user_input_string.split(" ")

d = {}
for j in list_of_words:
    if j in d:
        d[j] += 1
    else:
        d[j] = 1

print(d)
