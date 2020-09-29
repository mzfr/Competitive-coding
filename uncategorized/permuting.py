def twoArrays(k, A, B):
    for i in A:
        for j in B:
            if i+j >= k:
                A.remove(i)
                B.remove(j)
    if len(A) > 0 or len(B) > 0:
        return "NO"
    else:
        return "YES"
        
twoArrays(10, [2,1,3], [7,8,9])
