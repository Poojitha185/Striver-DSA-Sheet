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
