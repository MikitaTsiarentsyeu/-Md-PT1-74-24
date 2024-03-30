test_string = "His ex has bought this huge, detached house on a third of an acre. Rebecca listens, half dazed, half distracted with thoughts of her ex. She didn't want her ex- husband to outdo her."

vowels = ["a", "e", "u", "i", "o", "A", "E", "U", "I", "O"]
for i in test_string:
    if i in vowels:
        test_string = test_string.replace(i, "")

print(test_string)
