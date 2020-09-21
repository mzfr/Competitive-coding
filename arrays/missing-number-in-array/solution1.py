arr = []
for i in range(99):
    arr.append(int(input().strip('\r')))

current_sum = sum(arr)
n = len(arr)
total_sum = (n+1)*(n+2)//2

print(total_sum - current_sum)
