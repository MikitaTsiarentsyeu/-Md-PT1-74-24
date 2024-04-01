#3. Write a function that takes a list of strings as an argument and returns a new list with all the strings that have a length greater than 5.

#First option 

def str_length(a):
    return[i for i in a if len(i)>5]


input_str = str_length(["yellow", "blue", "red", "violet", "orange", "terracota", "hazel"])
print(input_str)

#Second option

def str_length2(b):
    long_str = []
    for string in b:
        if len(string) > 5:
            long_str.append(string)
    return long_str

input_str2 = str_length2(["yellow", "blue", "red", "violet", "orange", "terracota", "hazel"])
print(input_str2)
