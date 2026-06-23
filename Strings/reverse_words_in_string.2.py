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