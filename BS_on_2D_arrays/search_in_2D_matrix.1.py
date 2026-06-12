#Time Complexity: O(n × log m), We go through each of the `n` rows once. For any valid row where the target can exist, we apply binary search which takes O(log m). So overall time = O(n × log m).

#Space Complexity: O(1), No extra space is used just a few integer variables for looping and binary search. So space complexity is constant.

#If matrix[i][0] <= target && target <= matrix[i][m-1]: If this condition is met, we can conclude that row i has the possibility of containing the target.
#So, we will apply binary search on row i, and check if the ‘target’ is present. If it is present, we will return true from this step. Otherwise, we will return false.

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