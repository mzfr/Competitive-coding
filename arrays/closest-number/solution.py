arr = list(map(int, input().split()))
arr.sort()
low = 9999999
pairs = []

for i in range(len(arr)-1):
    diff = abs(arr[i]-arr[i+1])
    if diff < low:
        low = diff

for i in range(len(arr)-1):
    if abs(arr[i+1] - arr[i]) == low:
        pairs.append(arr[i])
        pairs.append(arr[i+1])

print(" ".join(map(str, pairs)))
