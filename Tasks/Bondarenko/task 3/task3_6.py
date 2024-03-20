vowels = ["a", "e", "i", "o", "u", "y"]

vowels_count = 0

string = "Good morning!"
string = string.lower()

for i in vowels:
    string = string.replace(i, "")

print(f"string with out vowels = {string}")