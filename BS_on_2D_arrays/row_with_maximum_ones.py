def row_maximum_ones(matrix,n,m):
    cnt_max=0
    index=-1
    for i in range(n):
        cnt_ones=0
        for j in range(m):
             cnt_ones+=matrix[i][j]
        if cnt_ones>cnt_max:
            cnt_max=cnt_ones
            index=i
    return index
rows = int(input("Enter number of rows: "))
matrix = []
for i in range(rows):
    row = list(map(int, input().split(',')))
    matrix.append(row)
cols = len(matrix[0]) if matrix else 0
print(" The row with the maximum number of ones is:",row_maximum_ones(matrix,rows,cols))