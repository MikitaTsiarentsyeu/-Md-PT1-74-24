import time

def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper

def test_func():
    print("simple test func")

twice_test_func = do_twice(test_func)
twice_test_func()

test_func = do_twice(test_func)
test_func()

@do_twice
def check_access(func):
    password = "test"
    def wrapper():
        in_pass = input("please enter the password:\n")
        if in_pass == password:
            func()
        else:
            print("incorrect password")
    return wrapper

# test_func = check_access(test_func)
test_func()

def test_decor(func):
    def wrapper(*args):
        print("before")
        res = func(*args)
        print("after")
        return res
    return wrapper

def time_it(func):
    def wrapper(*args):
        global timed
        start = time.time()
        res = func(*args)
        finish = time.time()
        timed = finish-start
        return res
    return wrapper

@time_it
def sum(a, b):
    return a + b

print(sum(2, 3))
print(timed)