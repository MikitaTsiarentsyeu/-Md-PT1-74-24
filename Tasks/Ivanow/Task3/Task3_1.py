st = input('Enter expression:\n')
num_vowels = 0

vowels = list('aeiouy')

for letter in st:
    if letter in vowels:
        num_vowels += 1

print(f'Vowels number: {num_vowels}')