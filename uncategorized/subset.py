cases = int(input())

for _ in range(cases):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    count = 1
    for i in range(1, n):
        if arr[i] - arr[i-1] != 1:
            count += 1
    print(count)
