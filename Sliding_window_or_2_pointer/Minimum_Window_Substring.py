def minimum_window_substring(s,t):
    mincount=float('inf')
    substring=''
    for i in range(len(s)):
        for j in range(i,len(s)):
         for k in t:
            if k not in s[i:j+1] or s[i:j+1].count(k) < t.count(k):
             break
         else:
            if mincount>j-i+1:
              substring=(s[i:j+1])
              mincount=j-i+1
    return substring
s=input("Enter the string s: ")
t=input("Enter the string t: ")
result=minimum_window_substring(s,t)
print("The minimum window substring is:",result)
            


