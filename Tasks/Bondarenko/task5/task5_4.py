def get_low_up_chars_in_str(func_str):
    low, up = 0, 0
    for i in func_str: 
        if i == i.lower() and i != " ": low += 1
        if i == i.upper() and i != " ": up += 1
    return [low, up]

str = "HeLLo wOrLd"
print(str)
print(f"Low chars {get_low_up_chars_in_str(str)[0]}, up chars {get_low_up_chars_in_str(str)[1]}")