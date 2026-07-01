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
if __name__ == "__main__":
    sol = Solution()
    s = "(1+(2*3)+((8)/4))+1"
    result = sol.maxDepth(s)
    print("Max Depth:", result)
