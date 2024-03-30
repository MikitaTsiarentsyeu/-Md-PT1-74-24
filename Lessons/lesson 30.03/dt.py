# def sum(a, b):
#     return a+b

# def sum(a, b, c):
#     return sum(sum(a, b), c)

# sum(1,2,3) error!

def times(a, b):
    return a*b

print(times(2, 3))
print(times('2', 3))
print(times([2], 3))

def times_for_int(a:int, b:int) -> int:
    "this function will multiply only int objects"
    if isinstance(a, int) and isinstance(b, int):
        return a*b
    
print(times_for_int(2, 3))
print(times_for_int('2', 3))
print(times_for_int([2], 3))

def eq(coll1, coll2):
    for i in coll1:
        if i not in coll2:
            return False
    for i in coll2:
        if i not in coll1:
            return False
    return True

print(eq([1,2,3], (1,2,3)))
print(eq(['1','2','3'], "123"))