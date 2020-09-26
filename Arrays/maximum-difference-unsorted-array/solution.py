arr = [80, 2, 3, 6, 100, 1, 10, 5, 20]

maxdiff = arr[1]-arr[0]
min_ = arr[0]

for i in arr:
    if i - min_ > maxdiff:
        maxdiff = i - min_
    if i < min_:
        min_ = i
print(maxdiff)
