# Time Complexity: O(26*2N) = O(N), because for every shrinking step, we traverse 26 characters to update maxfreq.
# Space Complexity: O(1), because the dictionary stores at most 26 characters.

def longest_character_replacement(s, k):
    l,r,maxlen=0,0,0
    maxfreq=0
    dic={}
    while(r<len(s)):
        dic[s[r]]=dic.get(s[r],0)+1
        maxfreq=max(maxfreq,dic[s[r]])

        while((r-l+1)-(maxfreq)>k):                     #tc:o(n) overall bcz it travels entire string only once.so o(n)+o(n)=o(2n)
             dic[s[r]]=dic.get(s[r],0)-1
             maxfreq=0
             
             for i in range(26):                         #tc:o(26)
                 maxfreq=max(maxfreq,dic[s[r]])
             l=l+1
        if((r-l+1)-(maxfreq)<=k):
            maxlen=max(maxlen,r-l+1)
        r=r+1
    return maxlen

s=input("enter the string:")
k=int(input("enter the value of k:"))
print("The length of the longest substring after replacement is:",longest_character_replacement(s,k))


