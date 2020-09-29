    """https://practice.geeksforgeeks.org/problems/find-transition-point-1587115620/1
    """
def transitionPoint(arr, n):
    count = 0
    point = arr[0]
    
    if point == 1:
        return 0

    for i in arr:
        if i != point:
            return arr.index(i)
    return -1
