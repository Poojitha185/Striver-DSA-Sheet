#Time Complexity: O(N²), where N is the length of the string. For every starting index, the ending index can move toward the right until the substring becomes invalid.
#Space Complexity: O(1), because the frequency array stores counts for only 26 uppercase English letters.

def longest_character_replacement(s,k):
    n=len(s)
    maxlen=0                               # maxlen stores the length of the longest valid substring found so far.
    for i in range(n):
        dic={}
        maxfreq=0
        for j in range(i,n):
            dic[s[j]]=dic.get(s[j],0)+1
            maxfreq=max(maxfreq,dic[s[j]])
            changes=(j-i+1)-maxfreq
            if (changes<=k):
                maxlen=max(maxlen,j-i+1)
            else:
                break
    return maxlen

s=input("enter the string:")
k=int(input("enter the value of k:"))
print("The length of the longest substring after replacement is:",longest_character_replacement(s,k))

