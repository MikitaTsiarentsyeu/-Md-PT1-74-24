def count_lower_upper(some_string):
    lower = 0
    upper = 0
    for el in some_string:
        if el.islower():
            lower += 1
        elif el.isupper():
            upper += 1
    return lower, upper

string = "Write a Function That Takes a String as an Argument and Returns 2 Numbers."

low, up = count_lower_upper(string)

print(f"Lowercase letters {low}, uppercase letters {up}.")
