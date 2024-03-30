def case_type():
    while True:
        user_input = input('Please write your text: ')
        if user_input.lower() == "quit":
            break
        user_input = list(user_input)
        for i in range(len(user_input)):
            if user_input[i].islower():
                user_input[i] = user_input[i].upper()
            else:
                user_input[i] = user_input[i].lower()         
        print(''.join(user_input))
        
case_type()
   
    

    