start_count = "HeLLo WoRlD"

result = ""

for i in start_count:
    if i.isupper():
        result += i.lower()
    elif i.islower():
        result += i.upper()

print(result)

