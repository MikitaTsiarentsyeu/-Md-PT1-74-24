
vowels = ["a", "e", "i", "o", "u", "y"]

#solution 1
example = "Good morning!"
print(f"String {example} have {sum([1 for i in example.lower() for j in vowels if i == j])} vowels")

#solution 1.1
print(f"String {example} have {sum([1 for i in example.lower() if i in vowels])} vowels")

#solution 2
while True:
    vowels_count = 0

    string = input("write string: ")
    string = string.lower()

    for i in string:
        for j in vowels:
            if i == j:
                vowels_count = vowels_count + 1
                continue

    print(f"number of vowels in string = {vowels_count}")