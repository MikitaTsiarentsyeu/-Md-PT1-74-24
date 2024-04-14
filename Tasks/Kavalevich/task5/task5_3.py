def returns_greater_5(some_list):
    new_list = [el for el in some_list if len(el)>5]
    return new_list

my_list = ("Write a function that takes a list of strings as an argument and "
          "returns a new list with all the strings that have a length "
          "greater than 5.").split(' ')

print(returns_greater_5(my_list))
