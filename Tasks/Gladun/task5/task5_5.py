user_input = [0, 1, 2, 3, 4, 7, 8, 10]
# 0, 1, 2, 3, 4, 7, 8, 10
# 4,7,10
# 2, 3, 8, 9

def sort_range(user_input):
    l = 0
    j = 0
    ranges_list = []
    func_break = False
    for i in range(len(user_input)):
        if func_break == True:
            break
        if i == 0:
            l = user_input[i]
            if user_input[i] + 1 == user_input[i + 1]:
                j = user_input[i + 1]
            else:
                if i == len(user_input) - 1:
                    func_break = True
                    break
                if j == 0:
                    ranges_list.append(f"{l}")
                    l = 0
                else:
                    ranges_list.append(f"{l} - {j}")
                    l = 0
                    j = 0
        else:
            if i == len(user_input) - 1:
                if l == 0:
                    l = user_input[i]
                    ranges_list.append(f"{l}")
                else:
                    if j == 0:
                        ranges_list.append(f"{l}")
                        l = 0
                    else:
                        ranges_list.append(f"{l} - {j}")
                        l = 0
                        j = 0
                break
            if l == 0:
                l = user_input[i]
                if user_input[i] + 1 == user_input[i + 1]:
                    j = user_input[i + 1]
                else:
                    if j == 0:
                        ranges_list.append(f"{l}")
                        l = 0
                    else:
                        ranges_list.append(f"{l} - {j}")
                        l = 0
                        j = 0
            else:
                if user_input[i] + 1 == user_input[i + 1]:
                    j = user_input[i + 1]
                else:
                    if j == 0:
                        ranges_list.append(f"{l}")
                        l = 0
                    else:
                        ranges_list.append(f"{l} - {j}")
                        l = 0
                        j = 0
    print(ranges_list)

sort_range(user_input)
