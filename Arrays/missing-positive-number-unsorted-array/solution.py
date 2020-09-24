def segregate(arr):
    """Move all the negative number
     in the starting of the array

    Args:
        arr ([int]): the original array

    Returns:
        int: value of the point from which 
            positive number starts after sorting.
    """
    n = len(arr)
    j = 0
    for i in range(n):
        if arr[i] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return j

def findpositive(arr, n):
    """Find the postive number i.e THE ANSWER

    Args:
        arr (int): The array which contains only positive number
        n (int): Length of the new array.

    Returns:
        int: the missing value
    """
    for i in range(n):
        val = abs(arr[i])-1
        if val < n and arr[val] > 0:
            arr[val] = -arr[val]
    
    for i in range(n):
        if arr[i] > 0:
            return i+1
    
    return n+1

def main():
    arr = [3, 1, 4, 6, 7, -2, -8, -12, 10]
    seg = segregate(arr)
    print(findpositive(arr[seg:], n-seg))
    
if __name__ == "__main__":
    main()
