def level1():
    print("start of level 1")
    level2()
    print("end of level 1")

def level2():
    print("\tstart of level 2")
    level3()
    print("\tend of level 2")

def level3():
    print("\t\tstart of level 3")
    level4()
    print("\t\tend of level 3")

def level4():
    print("\t\t\tstart of level 4")
    level1()
    print("\t\t\tend of level 4")

# level1()

# def infinity():
#     while True:
#         print("infinity!")

# infinity()

def level(n=4):
    if n == 0:
        return
    print('\t'*(n-1)+f"start of level {n}")
    level(n-1)
    print('\t'*(n-1)+f"end of level {n}")

# level()


# 1! = 1
# 2! = 1*2
# 3! = 1*2*3
# 4! = 1*2*3*4
# 5! = 1*2*3*4*5
    
def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)

def loop_factorial(n):
    res = n
    while True:
        if n <= 1:
            break
        res *= n-1
        n -= 1
    return res

print(factorial(5))
print(loop_factorial(5))

# print(factorial(1001)) error
# print(loop_factorial(1001)) no error


l = [1,2,3, [4,5,6, [7,8,9, [10, [11, [12, [13, [14]]]]]]]]

# def flatten(l):
#     res = []
#     for i in l:
#         if not isinstance(i, list):
#             res.append(i)
#         else:
#             for j in i:
#                 if not isinstance(j, list):
#                     res.append(j)
#                 else:
#                     for k in j:
#                         if not isinstance(k, list):
#                             res.append(k)

#     return res

def flatten(l, res=[]):
    for i in l:
        if not isinstance(i, list):
            res.append(i)
        else:
            flatten(i, res)

    return res

print(flatten(l))


125

def digit_sum(num):
    if num == 0:
        return 0
    return digit_sum(num // 10) + (num % 10)

print(digit_sum(125))