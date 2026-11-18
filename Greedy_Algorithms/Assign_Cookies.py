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