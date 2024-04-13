user_input = str(input("please, enter your string \n")).lower()

vowels = ["a", "e", "i", "o", "u"]

count = 0
for i in user_input:
    if i in vowels:
        count += 1
print("number of vowels in your string = ", count)
