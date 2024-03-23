#First option

def word_counter():
   
    item_count = {}
    user_input = input('Enter your favorite quote: ')
    user_input = user_input.lower() 
    user_input = user_input.split()
    for i in user_input:
        i = i.strip(",.?!")
        if i in item_count:
            item_count[i] +=  1
        else:
            item_count[i] = 1
      
    print(item_count)
word_counter()

#Second option

from collections import defaultdict
my_string = "Today is a wonderful day!"
split_string = my_string.split()
res = defaultdict(int)
for i in split_string:
    res[i] += 1
print(res)
    

    