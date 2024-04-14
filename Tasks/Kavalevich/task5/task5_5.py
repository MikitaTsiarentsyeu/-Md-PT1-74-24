def get_ranges(ord_list):
    new_list = [[]]
    ind = 0
    i = 0
    while i != len(ord_list) - 1:
        for i in range(len(ord_list) - 1):
            if ord_list[i] + 1 != ord_list[i + 1]:
                if ord_list[i] not in new_list[ind]:
                    new_list[ind].append(ord_list[i])
                    ind = app_li(new_list, ind)
                else:
                    ind = app_li(new_list, ind)
                    new_list[ind].append(ord_list[i + 1])
            elif ord_list[i] + 1 == ord_list[i + 1]:
                if ord_list[i] not in new_list[ind]:
                    new_list[ind].append(ord_list[i])
                if ord_list[i + 1] not in new_list[ind]:
                    new_list[ind].append(ord_list[i + 1])
            else:
                ind = app_li(new_list, ind)
        break
    return new_list


def app_li(li, i):
    li.append([])
    i += 1
    return i


def ranges_numbs(sort_li):
    string = ""
    for i in range(len(sort_li)):
        start = str(sort_li[i][0])
        if len(sort_li[i]) == 1:
            string += start + ' '
        else:
            end = str(sort_li[i][-1])
            string += start + '-' + end + ' '
    string = string.rstrip().replace(' ', ', ')
    return string


my_list = [1, 3, 4, 5, 11, 12, 13, 14, 18, 19, 20, 22]
sort_list = get_ranges(my_list)
print(ranges_numbs(sort_list))
