#Time Complexity: O(N+M), where N = given row number, M = given column number. We are starting traversal from (0, M-1), and at most, we can end up being in the cell (M-1, 0). So, the total distance can be at most (N+M). So, the time complexity is O(N+M).

#Space Complexity: O(1) as we are not using any extra space.

#We will do the following steps until row < n and col >= 0(i.e. while(row < n && col >= 0)):
#If matrix[row][col] == target: We have found the target and so we will return true.
#If matrix[row][col] > target: We need the smaller elements to reach the target. But the column is in increasing order and so it contains only greater elements. So, we will eliminate the column by decreasing the current column value by 1(i.e. col--) and thus we will move row-wise.
#If matrix[row][col] < target: In this case, We need the bigger elements to reach the target. But the row is in decreasing order and so it contains only smaller elements. So, we will eliminate the row by increasing the current row value by 1(i.e. row++) and thus we will move column-wise.
#eventhough we did not use binary search directly here but we are eliminating one row or one column in each step, which is similar to the way binary search eliminates half of the search space in each step. 
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
