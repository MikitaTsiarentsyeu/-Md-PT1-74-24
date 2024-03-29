example = "GooD MoRniNg!"
result = ""

for i in example:
    if i == i.lower():
        result += i.upper()
    elif i == i.upper():
        result += i.lower()

print(f"string {example} new string {result}")