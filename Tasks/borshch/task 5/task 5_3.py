l = ["cup", "table", "refrigerator", "curtain", "flask", "shirt"]

# solution 1
# def str_lengh(l):
    # new_list = []
    # for i in l:
        # if len(i) > 5:
            # new_list.append(i)
    # return new_list

# solution 2
def str_lengh(l):  # return list of strings greater than 5
    new_list = [x for x in l if len(x) > 5]
    return new_list
