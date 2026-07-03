#Time Complexity: O(n), where n is the length of the string.

#Space Complexity: O(1), as only constant extra space is used.
 
# We're interested in measuring how deeply nested the parentheses are at any point in the string. Each opening bracket indicates going deeper into a new level of nesting.
#Each closing bracket signals returning to the previous level of nesting.
#By tracking how deep we go at each step, we can monitor the peak nesting level

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
