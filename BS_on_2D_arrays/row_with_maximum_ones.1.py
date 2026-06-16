
class Solution:
    # Binary search to find the lower bound (first index where element >= x)
    def lower_bound(self, arr, n, x):
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
    def row_with_max_1s(self, matrix, n, m):
        cnt_max = 0   # Maximum number of 1s found so far
        index = -1    # Row index with the max 1s

        for i in range(n):
            # Calculate count of 1s using lower bound
            cnt_ones = m - self.lower_bound(matrix[i], m, 1)
            if cnt_ones > cnt_max:
                cnt_max = cnt_ones
                index = i
        return index  # Return row index with most 1s


# Driver code
if __name__ == "__main__":
    matrix = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
    n, m = 3, 3

    obj = Solution()
    print("The row with maximum no. of 1's is:", obj.row_with_max_1s(matrix, n, m))
