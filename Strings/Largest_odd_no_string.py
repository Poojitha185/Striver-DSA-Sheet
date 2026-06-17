class Solution:
    # Function to find the largest odd number that is a substring of given string 
    def largeOddNum(self, s: str) -> str:
        ind = -1
        
        # Iterate through the string from the end to beginning
        i = 0
        for i in range(len(s) - 1, -1, -1):
            # Break if an odd digit is found
            if (int(s[i]) % 2) == 1:
                ind = i
                break
        
        # Skipping any leading zeroes
        i = 0
        while i <= ind and s[i] == '0':
            i += 1
        
        # Return the largest odd number substring
        return s[i:ind + 1]

# Driver code
solution = Solution()
num = "504"
result = solution.largeOddNum(num)
print("Largest odd number:", result)