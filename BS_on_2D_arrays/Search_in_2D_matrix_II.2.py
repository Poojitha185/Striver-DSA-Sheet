def search(matrix,target,n,m):
    row=0
    col=m-1
    while(row<n and col>=0):
        if(matrix[row][col]==target):
            return True
        elif matrix[row][col]<target:
            row=row+1
        else:
            col=col-1
    return False
rows = int(input("Enter number of rows: "))
matrix = []
for i in range(rows):
    row = list(map(int, input().split(',')))
    matrix.append(row)
cols = len(matrix[0]) if matrix else 0
target = int(input("Enter the target element: "))
print("Is the target element present in the 2D array?",search(matrix,target,rows,cols))
