def countSubsequenceWithTargetSum(ind, sum, nums):
        # Base case: if sum is 0, one valid subsequence is found
        if sum == 0:
            return 1
        #Base case: if sum is negative or index exceeds array size
        if sum < 0 or ind == len(nums):
            return 0
        #Recurse by including current number or excluding it from the sum
        return countSubsequenceWithTargetSum(ind + 1, sum - nums[ind], nums) + countSubsequenceWithTargetSum(ind + 1, sum, nums)      #including and not including the current number in the subsequence
import ast

nums = ast.literal_eval(input("Enter the array: "))
target = int(input("Enter the target sum: "))
print("The number of subsequences with target sum is:", countSubsequenceWithTargetSum(0, target, nums))

