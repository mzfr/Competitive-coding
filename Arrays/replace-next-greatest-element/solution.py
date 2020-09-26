arr = [16, 17, 4, 3, 5, 2]
n = len(arr)
max_ = arr[n-1]
arr[n-1] = -1

for i in range(n-2, -1, -1):
    temp = arr[i]
    arr[i] = max_
    max_ = max(max_, temp)
print(arr)
