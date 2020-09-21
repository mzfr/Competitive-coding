k = int(input())
array = list(map(int, input().split()))
array.sort()
i = 0
j = 1
count = 0

while i < len(array) and j < len(array):
    if i != j and array[j]-array[i] == k:
        count += 1
        i += 1
        j += 1
    elif array[j]-array[i] < k:
        j += 1
    else:
        i += 1
print(count)
