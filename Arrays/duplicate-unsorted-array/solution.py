arr = list(map(int, input().split()))
n = len(arr)

for i in range(n):
    ind = arr[i]%n
    arr[ind] += n

for i in arr:
    print(i, i//n)
    if (i//n) >= 1:
        print(i)
        