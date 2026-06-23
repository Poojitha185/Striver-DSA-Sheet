#Time Complexity: O(N), We traverse the string once from right to left and construct the result directly without extra passes.

#Space Complexity: O(1),Ignoring the output string, no additional data structures proportional to input size are used.

#Initialize an empty result string.Set a pointer at the last character of the string. While the pointer is within the string:. Skip all spaces to move to the end of a word. Mark the end position of the word.

#Move the pointer backward until a space or start of string is found.

#Extract the word and append it to the result string.

def reverse(s):
    result=""
    i=len(s)-1
    while i>=0:
        while i>=0 and s[i]==" ":
            i=i-1
        if i<0:
            break
        end=i
        while i>=0 and s[i]!=" ":
            i-=1
        w=s[i+1:end+1]
        if result!="":
              result+=" "
        result+=w
    return result
s=input("enter string:")
print("reversing of string:"+reverse(s))           #to get output acc to code without leading and trailing spaces we use concatenation(+) instead of (,) using print() function directly as it adds leading and trailing spaces in output.