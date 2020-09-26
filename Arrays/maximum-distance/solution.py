arr = [23, 21, 3, 5, 6, 8, 20, 2, 1]
n = len(arr)-1
lmin = [0]*(n+1)
rmax = [0]*(n+1)

lmin[0] = arr[0]
for i in range(1, n+1):
    lmin[i] = min(lmin[i-1], arr[i])

rmax[n] = arr[n]
for i in range(n-1, -1, -1):
    rmax[i] = max(rmax[i+1], arr[i])

i = j = count = 0

while j<=n and i<=n:
    if lmin[i] <= rmax[j]:
        count = max(count, j-i)
        j += 1
    else:
        i += 1
print(count)
