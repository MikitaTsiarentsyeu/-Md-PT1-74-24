def remove_vowels(string):
    return ''.join(char for char in string if char.lower() not in 'aeiou')

user_input = input("Enter a string: ")
result = remove_vowels(user_input)
print("String with vowels removed:", result)