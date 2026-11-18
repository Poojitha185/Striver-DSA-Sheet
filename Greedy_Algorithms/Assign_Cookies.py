#Time Complexity: O(n log n + m log m), where n is the number of children and m is the number of cookies. Sorting both arrays dominates the runtime.Sorting g → O(m log m) ,Sorting s → O(n log n)  while loop → O(m + n), So: O(m log m + n log n + m + n). The sorting terms dominate, therefore: Final TC = O(m log m + n log n)
#Space Complexity: O(1) because only constant space is used.Python's sort() uses some internal memory, so the auxiliary space is: SC = O(m + n) in the worst case.


def assign_cookies(g,s):
    m=len(g)
    n=len(s)
    g.sort()
    s.sort()
    l,r=0,0
    while(l<m and r<n):
        if g[l]<=s[r]:
            r=r+1
        l=l+1
    return r
g=list(map(int,input("Enter the greed factors of children: ").split(',')))
s=list(map(int,input("Enter the sizes of cookies: ").split(',')))
print("The maximum number of children that can be satisfied with the given cookies is:",assign_cookies(g,s))