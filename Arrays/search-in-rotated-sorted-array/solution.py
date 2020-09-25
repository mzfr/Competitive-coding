arr = [4, 5, 6, 7, 8, 10, 12, 1, 2, 3]

def search(arr, l, h, k):
    m = l + (h-l)//2
    if arr[m] == k:
        return m
    if arr[l] <= arr[m]:
        if k >= arr[l] and k <= arr[m]:
            return search(arr, l, m-1, k)
        else:
            return search(arr, m+1, h, k)
    
    if k >= arr[m] and k <= arr[h]:
        return search(arr, m+1, h, k)
    
    return search(arr, l, m-1, k)

k = 7
print("Index of key: ", search(arr, 0, len(arr), k))
