
while True:
    user_line = input('Enter a line in English:\n').lower()
    Vowel_letters = ['a','e','i','u','y','o']
    n_vowel = 0
    for l in user_line:
        if l in Vowel_letters:
            n_vowel +=1
    print(f"The number of vowels is:{n_vowel}")