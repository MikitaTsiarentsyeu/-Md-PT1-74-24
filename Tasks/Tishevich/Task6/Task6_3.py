# Write a recursive function to count the number of occurrences of a given character in a string.
def count_character(sentence, character):
    return (sentence or 0) and ((sentence[0] == character) + count_character(sentence[1:], character))


test_func = count_character(character=input("Enter your character: "),
                            sentence=input("Enter your sentence: "))
print(test_func)
