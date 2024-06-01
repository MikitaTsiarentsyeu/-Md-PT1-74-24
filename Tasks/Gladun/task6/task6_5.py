c = int(input())

def fibonacci(c):
    if c <= 1:
        return c
    else:
        return fibonacci(c-1) + fibonacci(c-2)

print(fibonacci(c))