def pairs(k, arr):
    _dict = Counter(arr)
    count = 0

    for i in arr:
        count += _dict[i+k]
    return count

k = int(input())
array = input().split()
print(pairs(k,array))

