arr = [2, 8, 7, 0, 0, 3, 6, 0, 0, 1]
c = 0
n = len(arr)
for i in range(n):
    if arr[i] != 0:
        arr[c] = arr[i]
        c += 1
while(c < n):
    arr[c] = 0
    c += 1
print(arr)
