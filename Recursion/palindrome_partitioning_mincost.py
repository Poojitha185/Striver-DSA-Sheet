#TC:number of recursive states/partitions × choices per state × palindrome checking = 2ⁿ × n × n.

#SC:Your space complexity remains O(n) because of the recursion stack.

def palindrome_partitoning(i,n,s):
    if i==n:
        return 0
    min_cost=float('inf')
    for j in range(i,n):
        if(ispalindrome(i,j,s)):
           cost=1+palindrome_partitoning(j+1,n,s)
           min_cost=min(cost,min_cost)
    return min_cost
def ispalindrome(i,j,s):
    while(i<j):
        if s[i]!=s[j]:
           return False
        i=i+1
        j=j-1
    return True
s=input("enter the string: ")
n=len(s)
print(palindrome_partitoning(0,n,s)-1)