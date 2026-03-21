#pointer approach
#TC:O(N) You compare characters from both ends Recursion runs until middle → n/2 calls
#SC:O(N) because of the recursive stack
def ispalindrome(i,n,str):       
    if i>=n/2:
        return True
    if  str[i]!=str[n-i-1]:  
        return False
    return ispalindrome(i+1,n,str)
str=input("enter the string to check: ")
n=len(str)
print(ispalindrome(0,n,str))