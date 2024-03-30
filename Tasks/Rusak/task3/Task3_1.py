def count_vowels(string):
    return sum(1 for char in string if char.lower() in "aeiou")

user_input = input("Enter a string: ")
print("Number of vowels:", count_vowels(user_input))
