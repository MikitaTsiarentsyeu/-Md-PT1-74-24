
while True:
    user_line = input('Enter a line in English:\n').lower()
    Vowel_letters = ['a','e','i','u','y','o'] 
    for i in Vowel_letters:
        user_line = user_line.replace(i,'')
    print(f"String with out vowels = {user_line}")
