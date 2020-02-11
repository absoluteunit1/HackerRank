def diagonalDifference(arr):
    n = len(arr)
    sm1 = 0
    sm2 = 0
    for i in range(n):
        sm1 += arr[i][i]
        sm2 += arr[i][(n-1)-i]
    return abs(sm1-sm2)