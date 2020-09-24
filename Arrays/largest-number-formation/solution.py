# arr = ["55", "566", "66", "9"]
arr = ["2", "34", "4", "97", "9", "75", "46", "3"]
n = len(arr)
bigloop = (n-1)*3

while bigloop:
    for i in range(n-1):
        if int(arr[i]+arr[i+1]) < int(arr[i+1]+arr[i]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    bigloop -= 1
print("".join(arr))
