#Time Complexity:O(n X logm), where n = given row number, m = given column number. We are using a loop running for n times to traverse the rows. Then we are applying binary search on each row with m columns.

#Space Complexity: O(1), no extra space is used.

#We will use Binary Search to make our solution more efficient. While we still need to check each row one by one, we can speed up how we count the 1s in each row. Instead of going through every element in a row to count the 1s, we find the position of the first 1 using Binary Search, and subtract that index from the total number of columns to get how many 1s are present.

def lower_bound(arr, n, x):
    low, high = 0, n - 1
    ans = n  # Default if x not found
    while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = mid       # Potential answer found
                high = mid - 1  # Look on the left half
            else:
                low = mid + 1   # Move right
    return ans  # Return index of first element >= x

    # Function to find the row with maximum number of 1s
def row_with_max_1s(matrix, n, m):
        cnt_max = 0   # Maximum number of 1s found so far
        index = -1    # Row index with the max 1s

        for i in range(n):
            # Calculate count of 1s using lower bound
            cnt_ones = m - lower_bound(matrix[i], m, 1)
            if cnt_ones > cnt_max:
                cnt_max = cnt_ones
                index = i
        return index  # Return row index with most 1s
rows = int(input("Enter number of rows: "))
matrix = []
for i in range(rows):
    row = list(map(int, input().split(',')))
    matrix.append(row)
cols = len(matrix[0]) if matrix else 0
print("The row with the maximum number of ones is:",row_with_max_1s(matrix, rows, cols))


