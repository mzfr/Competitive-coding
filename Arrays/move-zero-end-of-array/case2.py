arr = [2, 8, 7, 0, 0, 3, 6, 0, 0, 1]
n = len(arr)
c = n-1
for i in range(n-1, -1, -1):
    if arr[i] != 0:
        arr[c] = arr[i]
        c -= 1

while(c >= 0):
    arr[c] = 0
    c -= 1
print(arr)
