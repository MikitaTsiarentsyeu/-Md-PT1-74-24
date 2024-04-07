x = range(100)
print(type(x), x)

def bad_generator():
    yield 1
    yield 3.0
    yield "five"

gen1 = bad_generator()
gen2 = bad_generator()
print(gen1, type(gen1))

# for i in gen1:
#     print(i)

try:
    it = iter(gen1)
    while True:
        print(next(it))
except StopIteration:
    print("the end of the iteration")


def even_cubes(n):
    for i in range(n):
        if i % 2 == 0:
            yield i**3

# def even_cubes(n, res=[]):
#     for i in range(n):
#         if i % 2 == 0:
#             res.append(i**3)
#     return res

for i in even_cubes(10):
    print(i)



def fibonacci(n):
    a, b = 0, 1
    count = 0
    while True:
        yield a
        count += 1

        if count == n:
            break

        a, b = b, a + b


# def infinity():
#     while True:
#         yield "infinity!"

for i in fibonacci(10):
    print(i)


l = [1, 2, 3, [4, 5, [6, 7]], 8 , 9]

def flatten(l, res=[]):
    for i in l:
        if isinstance(i, list):
            flatten(i, res)
        else:
            res.append(i)
    return res

def flatten(l):
    for i in l:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i

for i in flatten(l):
    print(i)    



[x for x in range(10)]
{x for x in range(10)}
{x:str(x) for x in range(10)}

print((x for x in range(10)))

# def even_cubes(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield i**3

even_cubes = (i**3 for i in range(10) if i%2 == 0)
for i in even_cubes:
    print(i)