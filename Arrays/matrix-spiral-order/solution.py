arr = [[1,2,3,4],
       [12,13,14,5],
       [11,16,15,6],
       [10,9,8,7]
     ]

sr = 0
er = len(arr) # number of rows - 1
sc = 0
ec = len(arr[0]) # number of column - 1

while sr < er and sc < ec:
    for i in range(sc, ec):
        #print element from starting column to starting row
        print(arr[sr][i], end=" ")
    sr += 1 # increment the starting row

    for i in range(sr, er):
        print(arr[i][ec-1], end=" ")
    ec -= 1

    if sr < er:
        for i in range(ec-1, sc-1, -1):
            print(arr[er-1][i], end=" ")
        er -= 1

    if sc < ec:
        for i in range(er-1, sr-1, -1):
            print(arr[i][sc], end=" ")
        sc += 1



