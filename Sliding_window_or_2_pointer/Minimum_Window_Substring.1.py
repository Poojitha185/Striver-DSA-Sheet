#Time Complexity: O(N²), where N is the length of s. For every starting index, the ending index may move toward the right until a valid window is found.
#Space Complexity: O(1), because fixed-size frequency arrays are used for ASCII characters.

def minimum_window_substring(s,t):
    mincount=float('inf')
    startind=0
    for i in range(len(s)):
        cnt=0
        di={}
        for k in range(len(t)):
            di[t[k]]=di.get(t[k],0)+1
        for j in range(i,len(s)):
            if di.get(s[j], 0) > 0:
                cnt+=1
                di[s[j]]-=1
            if(cnt==len(t)):
                if(j-i+1<mincount):
                    mincount=j-i+1
                    startind=i
                    break
    if mincount == float('inf'):
       return ""
    return s[startind:startind+mincount]

s=input("Enter the string s: ")
t=input("Enter the string t: ")
result=minimum_window_substring(s,t)
print("The minimum window substring is:",result)



