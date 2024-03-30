import random

l = [34,56,7,9,76,4,123,56]

print(sorted(l), l)

# l.sort()
# print(l)

def random_sort(l):
    counter = 0
    while not is_sorted(l):
        # i = generate_index(len(l))
        # j = i
        # while j == i:
        #     j = generate_index(len(l))
        swap(l)
        counter += 1
    return counter


def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def generate_index(n):
    return random.randint(0, n-1)

def swap(l):
    i=generate_index(len(l))
    j=generate_index(len(l))
    l[i], l[j] = l[j], l[i]

print(random_sort(l), l)