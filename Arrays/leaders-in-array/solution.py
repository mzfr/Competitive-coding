_ = input()

arr = list(map(int, input().split()))
leaders = []
max_ = arr[-1]
leaders.append(max_)
for i in reversed(arr):
    if i > max_:
        leaders.append(i)
        max_ = i
output = list(reversed(leaders))
for i in output:
    print(i, end=" ")
