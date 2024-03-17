def word_counter():
   
    item_count = {}
    user_input = input('Enter your favorite quote: ')
    user_input = user_input.lower() 
    user_input = user_input.split()
    for i in user_input:
        if i in item_count:
            item_count[i] +=  1
        else:
            item_count[i] = 1
      
    print(item_count)
word_counter()
    