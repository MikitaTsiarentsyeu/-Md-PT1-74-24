#2. Write a function that takes a list of strings as an argument and returns a new list of strings that are all reversed.

#First option

def reverse_string_list(string_list):

    reversed_list = []  
    for string in string_list:  
        reversed_list.append(string[::-1])  
    return reversed_list

str_input = ["Hello, world", "Python", "is", "awesome"]
reversed_str_res = reverse_string_list(str_input)
print(reversed_str_res)

#Second option

def reverse_string_list2(string_list2):
    return [string[::-1] for string in string_list2]

str_input2 = ["Hello, world", "Python", "is", "awesome"]
reversed_str_res2 = reverse_string_list2(str_input)
print(reversed_str_res2)

#Third option

def reverse_string_list3(string_list3):
    reversed_list3 = []
    index = 0
    while index < len(string_list3):
        reversed_list3.append(string_list3[index][::-1])
        index += 1
    return reversed_list3

str_input3 = ["Hello, world", "Python", "is", "awesome"]
reversed_str_res3 = reverse_string_list3(str_input3)
print(reversed_str_res3)

