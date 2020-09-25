arr = [12, 22, 17, 4, 25, 92, 70]

def findpeak(arr, l, h, n):
    m = l + (h-l)//2
    if (m == 0 or arr[m-1] <= arr[m]) and (m == n-1 or arr[m+1] <= arr[m]):
        return m
    elif m > 0 and arr[m-1] > arr[m]:
        return findpeak(arr, l, m-1, n)
    else:
        return findpeak(arr, m+1, h, n)

n = len(arr)
print("Index of peak element: ", findpeak(arr, 0, n-1, n))
