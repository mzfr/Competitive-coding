arr = [23, 45, 12, 1, 4, 5]
n = len(arr)
print("Given array is: ", arr)

for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    print(arr)

print("Sorted array is: ", arr)
