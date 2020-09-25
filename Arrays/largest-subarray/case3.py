# arr = [12, 13, 14, -6, -2, -7, 2, 3, 5, 6]
arr = [0, 1, 1, 0, -2, -4, 0, 1, 0]
max_array = []
anew = []
count = 0

for i in arr:
    if i >= 0:
        anew.append(i)
    else:
        anew = []
    if len(anew) > len(max_array):
        max_array = anew
    if len(anew) == len(max_array):
        max_array = max(max_array, anew)
        
print(max_array)
