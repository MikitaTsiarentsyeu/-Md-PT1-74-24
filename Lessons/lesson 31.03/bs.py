
def search(l, target, low=0, high=None):
    if high == None:
        high = len(l)-1

    if high >= low:
        mid = (low + high) // 2
        if l[mid] == target:
            return mid
        elif l[mid] > target:
            return search(l, target, low, mid-1)
        else:
            return search(l, target, mid+1, high)
    else:
        return False
    

l = [2,3,5,7,9,10,11,13]

print(search(l, 5))