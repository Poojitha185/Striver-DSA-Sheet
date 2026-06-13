def binary_search(matrix,n,m,target):
    low,high=0,(n*m-1)
    while low<=high:
        mid=(low+high)//2
        row=mid//m
        col=mid%m
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]<target:
            low=mid+1
        else:
            high=mid-1
    return False
rows = int(input("Enter number of rows: "))
matrix = []
for i in range(rows):
    row = list(map(int, input().split(',')))
    matrix.append(row)
cols=int(input("Enter number of cols: "))
target = int(input("Enter the target element: "))
print("Is the target element present in the 2D array?",binary_search(matrix,rows,cols,target))