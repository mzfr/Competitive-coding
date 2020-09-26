arr = [-2, -3, 4, -1, -2, 1, 5, -3]

max_sf = max_eh = 0

for i in arr:
    max_eh += i 
    if max_eh < 0:
        max_eh = 0

    if max_sf < max_eh:
        max_sf = max_eh

print(max_sf)
