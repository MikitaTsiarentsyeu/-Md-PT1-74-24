st = input('Input some string:\n')
new_st = ''
vowels = list('aeiouy')

for letter in st:
    if letter in vowels:
        continue
    else:
        new_st += letter

print(new_st)