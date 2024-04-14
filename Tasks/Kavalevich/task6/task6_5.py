def fibonacci_n(numb):
    if numb == 1:
        return 0
    elif numb == 2:
        return 1
    else:
        return fibonacci_n(numb-1) + fibonacci_n(numb-2)
    
print(fibonacci_n(6))
