arr = list(map(int, input().split()))
x = 0
y = 0
for i in arr:
    x = x^i
for j in range(1, len(arr)+2):
    y = y^j
print(x^y)
