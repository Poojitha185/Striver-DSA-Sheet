#Time Complexity:O(n X m), where n = given row number, m = given column number. We are using nested loops running for n and m times respectively.

#Space Complexity: O(1). No extra space used
#First, we create two variables: cnt_max is set to 0 and will keep track of the highest number of 1s found so far, and index is set to -1 and will store the row number with the most 1s.
#Then, we go through each row of the matrix one by one using a loop.
#Inside that loop, for each row, we count how many 1s it contains using another loop.

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