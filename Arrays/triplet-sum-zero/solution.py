arr = [0, -1, 2, -3, 1]

arr.sort()
n = len(arr)
found = False
for i in range(n-1):
    l = i+1
    r = n-1
    x = arr[i]

    while (l < r):
        sum_ = x + arr[l] + arr[r]
        if sum_ > 0:
            r -= 1
        elif sum_ < 0:
            l += 1
        else:
            print(x,arr[l], arr[r])
            l += 1
            r -= 1
            found = True
if not found:
    print("No triplet present")
