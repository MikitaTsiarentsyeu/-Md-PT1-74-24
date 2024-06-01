user_input = input("please, enter string: ")
user_input = user_input.lower()

result = str()

vowels = [ "a" , "e" , "u" , "i" , "y", "o"]

for i in user_input:
    if i not in vowels:
        result += i

print(result)