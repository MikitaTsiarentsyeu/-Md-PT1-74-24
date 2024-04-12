def test_func(a, b, c):
    print(f"a={a}, b={b}, c={c}")

test_func(1,2,3)

def oper(a, b, sign='+'):
    if sign == '+':
        return a+b
    elif sign == '*':
        return a*b
    
print(oper(b=2, a=3))
print(oper(2, 3, '*'))

def test_func(a=0, b=1, c=2):
    print(f"a={a}, b={b}, c={c}")

test_func(2, 3)
test_func(c=5, b=3)


def sum(*args):
    print(type(args), args)
    res = 0
    for i in args:
        res += i

    return res

print(sum(1,2,3,4,5,90))

def test_args(a, b, *args, c, d):
    print(a, b, args, c, d)

test_args(1,2,3,4,5,6,7,c=8,d=9)

def test_kwargs(a, b, *args, c="test", **kwargs):
    # print(type(kwargs), kwargs)
    print(a, b, args, c, kwargs)

test_kwargs(5, 6, 7,8,9, d=2, test="test")


def test_append(l=[], val=0):
    print(id(l))
    l.append(val)
    return l

print(test_append(val="test"))
print(test_append(val="new value"))