#Time Complexity: O(N + M), where N is the length of s and M is the length of t. The string t is processed once, and every character of s enters and leaves the sliding window at most once.
#Space Complexity: O(1), because fixed-size frequency arrays are used for ASCII characters.

def minimum_window_substring(s,t):
    mincount=float('inf')
    startind=0
    l=0
    r=0
    cnt=0
    di={}
    for k in range(len(t)):
        di[t[k]]=di.get(t[k],0)+1
    while(r<len(s)):
        if s[r] in di:
           if di[s[r]] > 0:
             cnt+=1
           di[s[r]]-=1
        while(cnt==len(t)):
            if(r-l+1<mincount):
                    mincount=r-l+1
                    startind=l
            if s[l] in di:
                  di[s[l]] += 1
                  if di[s[l]] > 0:
                    cnt -= 1
            l=l+1
        r=r+1
    if mincount == float('inf'):
       return ""
    return s[startind:startind+mincount]

s=input("Enter the string s: ")
t=input("Enter the string t: ")
result=minimum_window_substring(s,t)
print("The minimum window substring is:",result)
