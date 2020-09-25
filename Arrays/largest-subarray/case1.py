# arr = [12, 13, 14, -6, -2, -7, 2, 3, 5, 6]
arr = [0, 1, 1, 0, -2, -4, 0, 1, 0]
max_length = 0
count = 0

for i in arr:
    if i >= 0:
        count += 1
    else:
        max_length = max(max_length, count)
        count = 0
    max_length = max(max_length, count)

print(max_length)
