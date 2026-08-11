#Time Complexity:  O(N² × 2ᴺ) There can be up to 2^(N-1) possible partitions.For every possible substring, ispalindrome() can take O(N) in the worst case.At the base case:ans.append(cur[:])you copy the current partition, which can contain up to N strings, costing up to O(N).
#Space Complexity: O(N × 2ᴺ)  Because you store all possible palindrome partitions in ans.There can be exponentially many partitions, and each partition can contain up to N strings.Number of partitions → O(2ᴺ)Size of each partition → O(N)
#Auxiliary Space: O(N)        ← recursion + current partition
# 1.Start from index i and try all possible ending positions j.
# 2.Check whether the substring s[i:j+1] is a palindrome.
# 3.If it is a palindrome, add the substring to cur.
# 4.Recursively partition the remaining string from j+1.
# 5.If i reaches n, add a copy of cur to ans.
# 6.Backtrack by removing the last added substring from cur.

def palindrome_partitoning(i,n,s,ans,cur):
    if i==n:
        ans.append(cur[:])     #cu[:]->copy the entire list
        return 
    for j in range(i,n):
        if(ispalindrome(i,j,s)):
           cur.append(s[i:j+1])
           palindrome_partitoning(j+1,n,s,ans,cur)
           cur.pop()
def ispalindrome(i,j,s):
    while(i<j):
        if s[i]!=s[j]:
           return False
        i=i+1
        j=j-1
    return True

s=input("enter the string: ")
ans=[]
cur=[]
n=len(s)
palindrome_partitoning(0,n,s,ans,cur)
print(ans)