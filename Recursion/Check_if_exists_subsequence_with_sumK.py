
def checkIfExists(i, n, arr, k):
        # Base case: if the sum k is 0, a subsequence is found
        if k == 0:
            return True
        # Base case: if k is negative, no valid subsequence can be found
        if k < 0:
            return False
        # Base case: if all elements are processed, check if k is 0
        if i == n:
            return k == 0       #k==0 is a boolean expression that evaluates to True if k is 0,and False if k is not equal to zero and index reaches n
                                #if i==n: return False, instead of checking k==0 we can directly return False after index i reaches n bcz if it equals to zero after reaches n it is check by k==0 condition at first and thereby return True so no need to check again
        
        # Recursive call: include the current element in the subsequence
        # or exclude the current element from the subsequence
        return checkIfExists(i + 1, n, arr, k - arr[i]) or checkIfExists(i + 1, n, arr, k)
import ast
nums = ast.literal_eval(input("Enter the array: "))
target = int(input("Enter the target sum: "))
print("Does a subsequence with the target sum exist?", checkIfExists(0, len(nums), nums, target))

