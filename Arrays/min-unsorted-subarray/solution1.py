arr = list(map(int, input().split()))
n = len(arr)
# Find the left most element which
# will be the starting of unsorted array
for l in range(n-1):
    if arr[l] > arr[l+1]:
        break

if l == n-1:
    print('Sorted array')

# Find the ending of unsorted array
for r in range(n-1, 0, -1):
    if arr[r] < arr[r-1]:
        break

max_ = arr[l]
min_ = arr[r]

# We sort the unsorted section
for i in range(l+1, r+1):
    if arr[i] > max_:
        max_ = arr[i]
    if arr[i] < min_:
        min_ = arr[i]

# Check if any element in LHS sorted section is greater than min
for i in range(0,l):
    if arr[i] > min_:
        l = i
        break

# Check if any element in RHS sorted section is smaller than max
for i in range(n-1, r,-1):
    if arr[i] < max_:
        r = i
        break

print("starting index of unsorted array: ", l)
print("last index of unsorted array: ", r)
