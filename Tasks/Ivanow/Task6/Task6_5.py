
def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


fib_res = [fibonacci(i) for i in range(5)]
for i in fib_res:
    print(i)