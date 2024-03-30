st = input('Input your string:\n')
st_new = ''
for letter in st:
    if letter == letter.lower():
        letter = letter.upper()
        st_new += letter
    else:
        letter = letter.lower()
        st_new += letter

print(st_new)