mat = [ [10, 20, 30, 40], 
        [15, 25, 35, 45], 
        [27, 29, 37, 48], 
        [32, 33, 39, 50] ] 

def bin_search(arr,low, high, x):
    """recursive function for binary search
    """
    if high>= low:
        mid = (low+high)//2

        if arr[mid] == x:
            return mid
        if x < arr[mid]:
            return bin_search(arr, low, mid-1, x)
        if x > arr[mid]:
            return bin_search(arr, mid+1, high, x)
    else:
        return -1
x = 39 # Element to find
i = 0
for row in mat:
    find = bin_search(row, 0, len(row)-1, x)
    if find == -1:
        i += 1
    else:
        print("Element at %d %d" % (i+1, find+1))
        break    
