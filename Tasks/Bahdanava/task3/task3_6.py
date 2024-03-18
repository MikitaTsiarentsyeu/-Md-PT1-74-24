# OPTION 1
def vowels_remove(string):

    x = ['a', 'e', 'y', 'u', 'i', 'o']
    string = list(string)
    new_string = []
    for i in string:
        if i.lower() not in x:
            new_string.append(i)
    print(''.join(new_string))

string = 'Today is a wonderful day'
vowels_remove(string)


# OPTION 2

x = ['a', 'e', 'y', 'u', 'i', 'o']
string = 'Today is a wonderful day'
xx = [i for i in string if i.lower() not in x]
print(''.join(xx))
