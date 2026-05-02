# This function returns the maximum product subarray
# using prefix and suffix traversal
class Solution:
    def maxProductSubArray(self, arr):
        # Store length of array
        n = len(arr)

        # Initialize prefix and suffix products
        pre, suff = 1, 1

        # Initialize answer as negative infinity
        ans = float('-inf')

        # Traverse from both front and back
        for i in range(n):
            # Reset prefix if zero
            if pre == 0:
                pre = 1

            # Reset suffix if zero
            if suff == 0:
                suff = 1

            # Multiply prefix with front element
            pre *= arr[i]

            # Multiply suffix with back element
            suff *= arr[n - i - 1]

            # Update maximum product so far
            ans = max(ans, pre, suff)

        # Return the result
        return ans

# Sample usage
arr = [2, 3, -2, 4]
sol = Solution()
print(sol.maxProductSubArray(arr))
