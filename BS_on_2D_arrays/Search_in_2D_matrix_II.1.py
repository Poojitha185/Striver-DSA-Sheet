def binary_search(row,m,target):
    low,high=0,m-1
    while low<=high:
        mid=(low+high)//2
        if row[mid]==target:
            return mid
        elif row[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
def search(matrix,target,n,m):
    for i in range(n):
        ind=binary_search(matrix[i],m,target)
        if ind!=-1:
            return (i,ind)
    return(-1,-1)
rows = int(input("Enter number of rows: "))
matrix = []
for i in range(rows):
    row = list(map(int, input().split(',')))
    matrix.append(row)
cols = len(matrix[0]) if matrix else 0
target = int(input("Enter the target element: "))
print("The target element is found at: ",search(matrix,target,rows,cols))

