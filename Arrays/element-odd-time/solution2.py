array = list(map(int, input().split()))
x = 0
for i in array:
    x = x ^ i
print(x)
