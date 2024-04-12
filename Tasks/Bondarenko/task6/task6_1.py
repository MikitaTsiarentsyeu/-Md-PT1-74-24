def reverse_string(string) -> str:
    if string == "":
        return string
    else:
        return string[-1] + reverse_string(string[:-1])

string = "hello world"
print(reverse_string(string))
