def uniquePaths(m:int, n:int):
    row = [1] * n

    for i in range(m-1):
        newRow = [1] * n
        for j in range(n-2,-1,-1):
            newRow[j] = row[j] + newRow[j+1]
        newRow = row
    return row[0]

