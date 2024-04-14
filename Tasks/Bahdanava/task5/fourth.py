#4. Write a function that takes a string as an argument and returns two numbers, first for count of lower case letters, second for count of the upper case letters in the initial string.

def case_count(a):
    lower_count = 0
    upper_count = 0
    for c in a:
        if c.islower():
            lower_count += 1
        elif c.isupper():
            upper_count += 1
    return lower_count, upper_count 

lower_count, upper_count = case_count("HeLlO and Happy New Year")
print("Количество букв нижнего регистра:", lower_count)
print("Количество букв верхнего регистра:", upper_count)