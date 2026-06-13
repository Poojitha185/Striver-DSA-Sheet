#Time Complexity: O(log(NxM)), where N = given row number, M = given column number.We are applying binary search on the imaginary 1D array of size NxM.

#Space Complexity: O(1) as we are not using any extra space.

#If we flatten the given 2D matrix into a 1D array, that 1D array would also be sorted. By running binary search on this flattened version, we could quickly check if the element exists.
#But actually flattening the matrix takes extra time and memory, which makes it inefficient. Instead, we can simulate the flattening without creating a new array. The trick is to directly map a 1D index into the corresponding row and column of the 2D matrix.
#To do this mapping, if there are `m` columns in the matrix and the index is `i`, then:
#Row = i // m, Column = i % m.

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