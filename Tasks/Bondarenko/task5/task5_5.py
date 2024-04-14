def ranges(a, n):
 
    length = 1
    list = []
     
    if (n == 0):
        return list
     
    for i in range (1, n + 1):
     
        if (i == n or a[i] -
            a[i - 1] != 1):
        
            if (length == 1):
                list.append(str(a[i - length]))
            else:
     
                temp = (str(a[i - length]) +
                        " - " + str(a[i - 1]))
                list.append(temp)

            length = 1
        
        else:
            length += 1
    return list
 
 
#list = [1, 2, 3, 4, 5, 6, 7, 9, 10, 44] 
list = [39, 40, 41, 42, 500, 100, 101, 102, 103, 104] 
n = len(list)
     
ans = ranges(list, n)
print ("[", end = "")
for i in range(len(ans)):
     
    if(i == len(ans) - 1):
        print (ans[i], "]") 
    else:
        print (ans[i], end = ", ")