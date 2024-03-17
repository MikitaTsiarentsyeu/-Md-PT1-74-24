def sum_numbers(x):
    n = 0
    for i in x:
        if i % 2 == 0:
            n += i 
    return n
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = sum_numbers(x)
print("The sum of even numbers: ", result)
        
     
        
    
