#Time Complexity: O(n), where n is the length of the string.

#Space Complexity: O(1), as only constant extra space is used.

class Solution:
    # Method to compute maximum depth of parentheses
    def maxDepth(self, s: str) -> int:
        p = 0  
        ans = 0
        for ch in s:
            # Increase depth on open parenthesis
            if ch == '(':
                p += 1
            # Decrease depth on close parenthesis
            elif ch == ')':
                p -= 1
            # Update maximum depth encountered
            ans = max(ans, p)
        return ans  

# Main test
if __name__ == "__main__":
    sol = Solution()
    s = "(1+(2*3)+((8)/4))+1"
    result = sol.maxDepth(s)
    print("Max Depth:", result)
