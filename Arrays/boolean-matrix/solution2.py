arr = [[1, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]

rflag = False
cflag = False

for i in range(4):
    for j in range(4):
        if i == 0 and arr[i][j] == 1:
            rflag = True
        if j == 0 and arr[i][j] == 1:
            cflag = True
        if arr[i][j] == 1:
            arr[0][j] = 1
            arr[i][0] = 1

for i in range(1, 4):
    for j in range(1, 4):
        if arr[0][j] == 1 or arr[i][0] == 1:
            arr[i][j] = 1

if rflag:
    for i in range(4):
        arr[0][j] = 1
if cflag:
    for i in range(4):
        arr[i][0] = 1
print(arr)
