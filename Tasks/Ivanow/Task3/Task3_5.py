st = list(input('Enter expression:\n'))

st.append(' ')
count = 0
new_st = list()
word = ''

for c in st:
    if c == ' ' or c == '!' or c == '.' or c == '?':
        if count >= 5:
            new_st.append(word)
        count = 0
        word = ''
    else:
        word += c
        count += 1

print(new_st)