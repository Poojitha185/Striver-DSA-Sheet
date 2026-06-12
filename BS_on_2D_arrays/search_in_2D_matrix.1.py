def binary_search(row,m,target):
    low,high=0,m-1
    while low<=high:
        mid=(low+high)//2
        if row[mid]==target:
            return True
        elif row[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return False
def search_matrix(matrix,target):
    n=len(matrix)
    m=len(matrix[0])
    for i in range(n):
        if matrix[i][0]<=target and matrix[i][m-1]>=target:
            return binary_search(matrix[i],m,target)
    return False   
rows = int(input("Enter number of rows: "))
matrix = []
for i in range(rows):
    row = list(map(int, input().split(',')))
    matrix.append(row)
target = int(input("Enter the target element: "))
print("Is the target element present in the 2D array?",search_matrix(matrix,target))