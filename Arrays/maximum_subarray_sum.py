from typing import List

class Solution:
    # Function to find maximum sum of subarrays
    def maxSubArray(self, nums: list[int]) -> int:
        
        """ Initialize maximum sum with
        the smallest possible integer"""
        maxi = float('-inf')

        # Iterate over each starting index of subarrays
        for i in range(len(nums)):
            
            """ Iterate over each ending index
            of subarrays starting from i"""
            for j in range(i, len(nums)):
                
                """ Variable to store the sum
                of the current subarray"""
                sum = 0

                # Calculate the sum of subarray nums[i...j]
                for k in range(i, j + 1):
                    sum += nums[k]

                """ Update maxi with the maximum of itscurrent
                value and the sum of the current subarray"""
                maxi = max(maxi, sum)

        # Return the maximum subarray sum found
        return maxi

# Test
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solution = Solution()
print("Maximum subarray sum:", solution.maxSubArray(arr))