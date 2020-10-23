arr = [4, 7, 1, 9, 3]
n = len(arr)
for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(arr)

print("sorted array is ", arr)
