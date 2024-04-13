#Count of a given character 

def char_count(a, i):
    if not a:
        return 0
    elif a[0].lower() == i.lower():  
        return 1 + char_count(a[1:], i)
    else:
        return char_count(a[1:], i)

input_string = "Hello WORLD!!!"
given_character = "l"
occurrences = char_count(input_string, given_character)
print(f"Occurrences of '{given_character}' in the string: {occurrences}")


#Count of all characters and punctuation marks sorted alphabetically(just to check if its correct)

def character_count(a):
    if not a:
        return {}
    elif a[0] == ' ':  
        return character_count(a[1:])
    else:
        count_i = character_count(a[1:])
        count_i[a[0]] = count_i.get(a[0], 0) + 1
        return count_i

input_string = "Hello world!!!"
result = character_count(input_string)
print("Occurrences of each character in the string: ")
for i, k in sorted(result.items()):
    print(f"'{i}': {k}")
