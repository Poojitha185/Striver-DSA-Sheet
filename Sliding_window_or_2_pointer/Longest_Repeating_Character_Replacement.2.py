#Time Complexity: O(N), where N is the length of the string. Each character is processed once by the right pointer, and the left pointer only moves forward.
#Space Complexity: O(1), because the frequency array stores counts for only 26 uppercase English letters.

#The optimal approach uses sliding window.The window represents the current substring that we are trying to convert into one repeating character.For a window to be valid, the number of characters that need replacement must be at most k.
#The best character to keep unchanged is the one with the maximum frequency inside the window. So: replacementsNeeded = window length - maxFrequency
#If replacementsNeeded becomes greater than k, the window is too large and must be adjusted from the left.
#A small optimization is used here: instead of shrinking the window repeatedly using a while loop, we shrink it by one position using an if condition. This works because the goal is to maintain the largest possible window size. When the window becomes invalid, adding one character from the right and removing one character from the left prevents the window from growing incorrectly.
#The maxFrequency value is not recomputed while shrinking. It may sometimes represent an older maximum frequency, but that is fine because it never causes us to miss the best answer. It helps maintain the maximum possible window length efficiently.

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


