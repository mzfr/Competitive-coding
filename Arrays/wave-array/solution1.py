array = list(map(int, input().split()))
n = len(array)

for i in range(0, n, 2):
    if i > 0 and array[i-1] > array[i]:
        array[i-1], array[i] = array[i], array[i-1]
    if i < n-1 and array[i] < array[i+1]:
        array[i], array[i+1] = array[i+1], array[i]
print(array)
