user_input = input("Please, enter the string: ")

def count(user_input):
    count_up = 0
    count_lower = 0

    for i in user_input:
        if i.isupper():
            count_up += 1
        elif i.islower():
            count_lower += 1

    print(f"count of lower {count_lower}, count of upper {count_up}")

count(user_input)