#First option

def sum_numbers(x):
    n = 0
    for i in x:
        if i % 2 == 0:
            n += i 
    return n
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = sum_numbers(x)
print("The sum of even numbers: ", result)
        
#Second option

x = [1, 3, 5, 7, 10, 2, 4, 6]
total_sum = sum(i for i in x if i % 2 == 0)
print(total_sum)   
        
    
