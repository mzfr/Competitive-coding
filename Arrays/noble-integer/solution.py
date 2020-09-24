arr = list(map(int, input().split()))

def noble(arr):
    arr.sort()
    n = len(arr)
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            continue
        if arr[i] == n-i-1:
            return arr[i]
    return -1

print(noble(arr))
