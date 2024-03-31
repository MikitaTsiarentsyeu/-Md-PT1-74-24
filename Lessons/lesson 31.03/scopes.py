x = "test"

# for x in range(10):
#     x+=1

print(x)

def test_scope():
    # x = 44
    # print(x)
    # x = 55
    print(x)

test_scope()
print(x)

global_value = 'global'

def test_func():
    global_value = "local"
    print(global_value)

test_func()
print(global_value)


def test_global():
    global global_value
    global_value = "new local value"
    print(global_value)

test_global()
print(global_value)


def outer():
    local_val = "outer"
    def inner():
        local_val = "inner"
        print(local_val)
    inner()
    print(local_val)

outer()