arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

crr = []

i = 0
j = 0
k = 0

# Check values at i and j and place accordingly
while i<len(arr) and  j < len(brr):
    if arr[i] < brr[j]:
        crr.append(arr[i])
        i += 1
    else:
        crr.append(brr[j])
        j += 1

# once the smaller array is finished then we find the remaining elements
# and insert them in the array as is.
if len(brr) > j:
    for x in brr[j:]:
        crr.append(x)
if len(arr) > i:
    for x in arr[i:]:
        crr.append(x)
print(crr)
