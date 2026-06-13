#Time Complexity: O(N X M), where N = given row number, M = given column number in order to traverse the matrix, we are using nested loops running for n and m times respectively.

#Space Complexity: O(1) as we are not using any extra space

#using linear search

def search(arr,n,m,target):
    for i in range(n):
        for j in range(m):
            if arr[i][j]==target:
                return True
    return False
rows = int(input("Enter number of rows: "))
matrix = []
for i in range(rows):
    row = list(map(int, input().split(',')))
    matrix.append(row)
cols = len(matrix[0]) if matrix else 0
target = int(input("Enter the target element: "))
print("Is the target element present in the 2D array?",search(matrix,rows,cols,target))