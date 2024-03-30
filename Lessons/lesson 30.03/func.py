

def test_sum(a, b):
    result = a+b
    return result

val = test_sum(2, 3)
print(val)


# test_print() error

def test_print():
    print("test print from test_print")

test_print()

def func1():
    print("this is func1")
    func2()

def func2():
    print("this is func2")

func1()

print(type(func1), id(func1), func1)

my_print = print
my_print("the same print function", id(my_print), id(print))

# def sum(a, b):
#     return a+b

def test_func(a, b, c):
    print(f"a={a}, b={b}, c={c}")

test_func(1,2,3)
test_func(3,2,1)

def test_int_obj(val):
    print(val, id(val))
    val+=2
    print(val, id(val))

my_val = 5
print(my_val, id(my_val))
test_int_obj(my_val)
print(my_val, id(my_val))


def test_list_obj(val):
    print(val, id(val))
    val[0]+=2
    print(val, id(val))

my_val = [5]
print(my_val, id(my_val))
test_list_obj(my_val)
print(my_val, id(my_val))


def test_func():
    return "test"
    print("after return")

test_func()

def oper(sign, a, b):
    if sign == '+':
        return a+b
    elif sign == '*':
        return a*b
    # else:
    #     return 0
    return

print(oper('+', 2, 3))    

print(oper('-', 3, 2))

def test_return():
    return 1,2,3,4,5,"test"

print(test_return())