def swap(a,b):
    a,b = b,a
    return a,b

arr = list(map(int, input().split()))

l = 0
mid = 0
h = len(arr)-1

while mid <= h:
    if arr[mid] == 0:
        arr[l], arr[mid] = swap(arr[l], arr[mid])
        l += 1
        mid += 1
    elif arr[mid] == 1:
        mid += 1
    elif arr[mid] == 2:
        arr[mid], arr[h] = swap(arr[mid], arr[h])
        h -= 1
print(arr)
