list_words = input("Write a text sentence:\n").lower().split(' ')

d = {}
for word in list_words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print(d)

