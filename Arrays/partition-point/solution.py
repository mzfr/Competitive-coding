def findElement(arr, n):
    leftMax = [None] * n 
    rightMin = [None] * n 
    
    leftMax[0] = -1
    for i in range(1, n):
        leftMax[i] = max(leftMax[i-1], arr[i-1])
    
    rightMin = 999999
    
    for i in range(n-1, -1, -1):
        if leftMax[i] < arr[i] and rightMin > arr[i]:
            return arr[i]
        rightMin = min(rightMin, arr[i])
    return -1

if __name__ == "__main__":
    array = list(map(int, input().split()))
    n = len(array)
    print(findElement(array, n))
