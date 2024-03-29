st = input('Enter expression:\n')
st += ' '
words = []
count = 0
word = ''
for i in st:
    if i == ' ':
        count += 1
        words.append(word)
        word = ''
        continue
    else:
        word += i

dictionary = {x + 1: words[x] for x in range(len(words))}
print(dictionary)