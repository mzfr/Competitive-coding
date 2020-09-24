arr = [(5,7), (2,3), (5,6)]
steps = 0
for i in range(len(arr)-1):
    dx = abs(arr[i][0] - arr[i+1][0])
    dy = abs(arr[i][1] - arr[i+1][1])
    steps += max(dx,dy)
print(steps)
