def word_count(string):
    words = string.split()
    return {word: words.count(word) for word in set(words)}

user_input = input("Enter a string: ")
print("Word frequency:", word_count(user_input))
