
 # Method to compute maximum depth of parentheses
def maxDepth(str):
        p = 0  
        ans = 0
        for ch in str:
            # Increase depth on open parenthesis
            if ch == '(':
                p += 1
            # Decrease depth on close parenthesis
            elif ch == ')':
                p -= 1
            # Update maximum depth encountered
            ans = max(ans, p)
        return ans  
str=input("Enter the string: ")
print("The maximum depth of nested parentheses is:", maxDepth(str))
