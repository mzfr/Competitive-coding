arr = [23, 45, 67, 1, 43, 78, 21, 4]
n = len(arr)

for i in range(n):
    min_ = i
    for j in range(i + 1, n):
        if arr[min_] > arr[j]:
            min_ = j
    arr[min_], arr[i] = arr[i], arr[min_]
    print(arr)
print("Sorted array is: ", arr)
