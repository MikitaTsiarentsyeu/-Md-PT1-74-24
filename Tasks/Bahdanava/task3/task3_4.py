def numbers_list(l):

    l = set(l)
    l = list(l)
    for j in range(len(l)-1):
        min_i = j
        for i in range(min_i + 1, len(l)):
            if l[i] < l[min_i]:
                min_i = i
        l[j], l[min_i] = l[min_i], l[j]

    print(l[-2])
    print(l)

l = [1, 3, 3, 9, 9, 5, 8, 7,7, 8, 15, 10]
numbers_list(l)

