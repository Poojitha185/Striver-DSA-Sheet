#Time Complexity: O(n × m), We are traversing the entire matrix with `n` rows and `m` columns. In the worst case, we may end up visiting every cell once if the target is not present. So, the total number of operations is proportional to the number of elements in the matrix.

#Space Complexity: O(1),We are not using any additional space. The algorithm uses a constant amount of extra memory regardless of the size of the matrix just loop variables and the target. Therefore, the space complexity is constant.

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