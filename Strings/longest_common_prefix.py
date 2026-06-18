class Solution:
    # Returns the longest common prefix from a list of strings
    def longestCommonPrefix(self, strs):
        # Handle empty list case
        if not strs:
            return ""
        
        # Sort the list lexicographically
        strs.sort()
        
        # First string in sorted list
        first = strs[0]
        
        # Last string in sorted list
        last = strs[-1]
        
        # Store the common prefix characters
        ans = []
        
        # Compare characters of first and last string
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