#First option

def string_length(string):

    new_string = []
    for i in string:
        if len(i) > 5:
            new_string.append(i)
    print(new_string)

string = ['Today', 'is', 'an', 'awesome', 'day', 'spring', 'started']
string_length(string)

#Second option:

x = ['today', 'is', 'an', 'extremely', 'amazing', 'daaayy']
new_x = [i for i in x if len(i) > 5]
print(new_x)

