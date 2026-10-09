
def longest_character_replacement(s, k):
    l,r,maxlen=0,0,0
    maxfreq=0
    dic={}
    while(r<len(s)):
        dic[s[r]]=dic.get(s[r],0)+1
        maxfreq=max(maxfreq,dic[s[r]])
        if((r-l+1)-(maxfreq)>k):
             dic[s[l]]=dic.get(s[l],0)-1
             l=l+1
        if((r-l+1)-(maxfreq)<=k):
            maxlen=max(maxlen,r-l+1)
        r=r+1
    return maxlen

s=input("enter the string:")
k=int(input("enter the value of k:"))
print("The length of the longest substring after replacement is:",longest_character_replacement(s,k))


