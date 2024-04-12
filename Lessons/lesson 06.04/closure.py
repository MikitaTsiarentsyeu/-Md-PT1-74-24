

# def outer():
#     def inner():
#         print("this is inner func")
#     # inner()
#     return inner


# new_func = outer()
# print(type(new_func), new_func)
# new_func()

def operator_factory(oper='+'):
    if oper == '+':
        def operator(a, b):
            return a+b
    elif oper == '-':
        def operator(a, b):
            return a-b
    elif oper == '*':
        def operator(a, b):
            return a*b
    elif oper == '/':
        def operator(a, b):
            return a/b
    else:
        return
    return operator

sum = operator_factory('*')
print(sum(2, 3))

def operator_factory(oper='+'):
    def operator(a, b):
        if oper == '+':
            return a+b
        elif oper == '-':
            return a-b
        elif oper == '*':
            return a*b
        elif oper == '/':
            return a/b
        else:
            return
    return operator

sum = operator_factory('*')
print(sum(2, 3))

def counter(n=1):
    def inner():
        # n+1
        nonlocal n
        n+=1
        return n+1
    return inner


from_10 = counter(10)
print(from_10())
print(from_10())


from_100 = counter(100)
print(from_100())
print(from_100())
print(from_10())