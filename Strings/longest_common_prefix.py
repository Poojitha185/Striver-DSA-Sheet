#Time Complexity: O(N * log N + M), where N is the number of strings and M is the minimum length of a string. The sorting operation takes O(N * log N) time, and the comparison of characters in the first and last strings takes O(M) time.

#Space Complexity: O(M), as the ans variable can store the length of the prefix which in the worst case will be O(M).

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        strs.sort()
        
        # First string in sorted list
        first = strs[0]
        
        # Last string in sorted list
        last = strs[-1]
        ans = []
        for i in range(min(len(first), len(last))):
            # Stop if characters differ
            if first[i] != last[i]:
                return ''.join(ans)
            # Add matching character to result
            ans.append(first[i])
        
        # Return the longest common prefix
        return ''.join(ans)

# Run the function with sample input
if __name__ == "__main__":
    # Create an instance of Solution
    solution = Solution()
    
    # Input list of strings
    input_strs = ["interview", "internet", "internal", "interval"]
    
    # Call the method to find prefix
    result = solution.longestCommonPrefix(input_strs)
    
    # Print the result
    print("Longest Common Prefix:", result)  