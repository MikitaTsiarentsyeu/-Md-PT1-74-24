list = [1, 100, 0, 20, 99, 100, 4, 67] 

max_number = max(list)
print(f"{max_number} is max number in list {list} ")
print(f"second max number {max([i for i in list if i != max_number])}")