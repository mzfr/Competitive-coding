mat = [ [10, 20, 30, 40], 
        [15, 25, 35, 45], 
        [27, 29, 37, 48], 
        [32, 33, 39, 50] ]
    
X = 49
n = len(mat)
row = 0
col = n-1
if X < mat[0][0] or X > mat[n-1][n-1]:
    print("Not found") 

while row < n and col > 0:
    if mat[row][col] > X:
        col -= 1
    elif mat[row][col] < X:
        row += 1
    else:
        print(row+1, col+1)
        break
if row > n-1 or col < 0:
    print("Not found")
