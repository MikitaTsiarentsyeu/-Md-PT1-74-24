st = input('Input your sting:\n')

new_st = ''

for letter in st[::-1]:
    new_st += letter

print(new_st)