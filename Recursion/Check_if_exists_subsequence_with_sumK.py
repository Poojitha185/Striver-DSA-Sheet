#Time Complexity: O(2^n), where n is the number of elements in the input array. This is because each element can either be included or excluded from the subsequence, leading to 2^n possible combinations.

#Space Complexity: O(n), where n is the depth of the recursion stack. In the worst case, the recursion can go as deep as n levels, leading to a space complexity of O(n) due to the call stack.

#Treat the problem as a decision tree where each item has two choices: include it or skip it.
#Recursively apply this decision process to the remaining items while updating the remaining target amount.
#Explore all possible combinations to determine if any subset matches the exact target.

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

