def length_of_substring(s):
    seen={}
    left,right=0,0
    maxlen=0
    while(right<len(s)):
        if s[right] in seen:
            if seen[s[right]]>=left:
                left=seen[s[right]]+1
        seen[s[right]]=right
        length=right-left+1
        maxlen=max(length,maxlen)
        right=right+1
    return maxlen
s=input("enter the string:")
print("The length of a longest substring without repeating characters: ",length_of_substring(s))

