# t = int(input())
# for i in range(t):
#     m,n = map(int, input().split())
#     arr = []
#     for i in range(m):
#         a = list(map(int, input().split()))
#         arr.append(a)
arr = [[1, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
m = 4
n = 4
r = [0]*m
c = [0]*n

for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            r[i] = 1
            c[j] = 1
        
for i in range(m):
    for j in range(n):
        if r[i] == 1 or c[j] == 1:
            arr[i][j] = 1
print(arr)
