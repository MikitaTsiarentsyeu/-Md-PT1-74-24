
def apply(l, func):
    for i in l:
        func(i)

apply([1,2,3,4,5], print)
apply("test", print)

def sq(x):
    print(x*x)

apply([1,2,3,4,5], sq)

test_str = "Abc Aac aaa"
print(sorted(test_str.split()))

print(ord('A'), ord('a'))

print(sorted([x.lower() for x in test_str.split()]))

print(sorted(test_str.split(), key=str.lower))

l = [(1, "one"), (3, "three"), (2, "two")]
print(sorted(l))

def key_second_elem(t):
    return t[1]

print(sorted(l, key=key_second_elem))

print(sorted(l, key=lambda x: x[1]))

sum = lambda x, y: x+y
print(sum(2, 3))

l = [1,2,3,4,5,6,7,8,9,10]
map_res = map(print, l)
print(map_res)

print(range(10))
# for i in map_res:
#     pass

res = [x for x in map_res]
print(res)

print(list(map(lambda num: chr(num*10), map(lambda num: num*10, l))))

print(list(map(lambda num: chr(num*10), filter(lambda num: num%2==0, l))))

from functools import reduce

print(reduce(lambda x, y: f"{x}-{y}", l))
"1-2"
"1-2-3"
"1-2-3-4"

print(reduce(lambda x, y: x if x<y else y, l))