# First option
def counter():
    while True: 
        vowels = ['a', 'e', 'y', 'u', 'i', 'o']
        user_input = input("Please write random adjectives without punctuation marks: ")
        user_input = str(user_input.lower())
        if user_input.lower() == 'quit':
            break
        else:
            n = 0
            for i in user_input:
                if i in vowels:
                    n = n+1
    print('Number of vowels: ', n)   
counter()


#Second option
vowels = ['a', 'e', 'y', 'u', 'i', 'o']
x = input("Write your string: ")
y = sum([1 for i in x if i in vowels])
print("The number of vowels is: ", y)



