#Time Complexity: O(N), we check for every number from 1 to N.
#Space Complexity: O(1), since the algorithm does not use any additional space or data structures.

class Solution:
    # Function to find floor of square root using linear search
    def floorSqrt(self, n: int) -> int:
        # Variable to store answer
        ans = 0

        # Run loop from 1 to n
        for i in range(1, n + 1):
            # Check if i*i <= n
            if i * i <= n:
                # Update answer
                ans = i
            else:
                # Break when i*i > n
                break

        # Return final answer
        return ans


# Example input
n = 27

# Create object of Solution
sol = Solution()

# Call function and print result
print(sol.floorSqrt(n))
