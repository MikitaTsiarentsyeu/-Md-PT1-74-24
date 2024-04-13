#func range


def func_rang (num_list:list):
    range_list = str(num_list[0])
    for i in range(1,len(num_list)):
        if num_list[i] - num_list[i-1] == 1 and  range_list[-1] != '-':
            range_list += '-'
            if num_list[i] == num_list[-1]:
                range_list += str(num_list[i])
        elif num_list[i] - num_list[i-1] > 1 and range_list[-1] == '-':
            range_list += str(num_list[i-1]) + ', ' + str(num_list[i])
        elif num_list[i] - num_list[i-1] > 1 and range_list[-1] != '-':
            range_list += (', ' + str(num_list[i]))
    return range_list

print(func_rang([0, 1, 2, 3, 4, 7, 8, 10])) # -> "0-4, 7-8, 10"
print(func_rang([4,7,10])) # -> "4, 7, 10"
print(func_rang([2, 3, 8, 9])) # -> "2-3, 8-9"
