#Time Complexity: O(n), since we are performing a single traversal of the string.

#Space Complexity: O(1), since we are using a few variables to track the current state.

#If the current character is '(', increment the level counter. If the level is greater than 1 (indicating we're inside a valid primitive), add '(' to the result string

#If the current character is ')', decrement the level counter. If the level is greater than 0 (indicating we're still inside a valid primitive), add ')' to the result string

def remove_outermost_parentheses(s):
    result=""
    level=0
    for char in s:
        if char=="(":
           if level>0:
               result+=char
           level+=1
        elif char==")":
            level-=1
            if level>0:
                result+=char
    return result
s=input("enter the string: ")
print("string after removing outermost parenthesis: ",remove_outermost_parentheses(s))
