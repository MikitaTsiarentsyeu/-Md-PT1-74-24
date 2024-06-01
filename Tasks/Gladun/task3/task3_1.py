vowels = [ "a" , "e" , "u" , "i" , "y", "o"]

count = 0

user_input = input(str("Enter the string: "))
user_input = user_input.lower()

for i in user_input:
    if i in vowels:
        count += 1
print("vowels in string: ", count)