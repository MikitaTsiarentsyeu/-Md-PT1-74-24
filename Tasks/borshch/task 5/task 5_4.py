string = "A string is a data type used in programming, that is used to represent text rather than numbers. A string is a sequence of characters and can contain letters, numbers, symbols and even spaces. It must be enclosed in quotation marks for it to be recognized as a string. For example, the word “liquid” and the phrase “What is liquid? It’s a template language.” are both strings. Even the sequence of characters “98OkJJ$%janUJ£” is considered a string."

def registr_count(string):  # counting separratly low and up letters
    dict = {"low": 0, "up": 0}
    for i in string:
        if i.isupper():
            dict["up"] += 1
        if i.islower():
            dict["low"] += 1
    return (dict["low"], dict["up"])
