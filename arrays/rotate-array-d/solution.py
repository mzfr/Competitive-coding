d = int(input())
arr = input().split()

result = arr[d:] + arr[:d]
print(" ".join(map(str, result)))

