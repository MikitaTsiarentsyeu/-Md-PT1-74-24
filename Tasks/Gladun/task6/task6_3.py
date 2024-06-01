user_input_string = str(input(" Enter the string: "))
user_input_symbol = str(input(" Enter the symbol: "))
count = 0

def count_symbol(m , l , count):
    for i in m:
        if i == l:
            count += 1
    return count

print(f"The character appears {count_symbol(user_input_string , user_input_symbol , count)} times in the string")