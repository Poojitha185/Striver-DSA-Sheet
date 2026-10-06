#Time Complexity: O(N), where N represents the string length. Pointer right processes every character once, while pointer left only moves forward.
#Space Complexity: O(N), because lastSeen may store an entry for every distinct character in the string.

#Instead of restarting from every index, maintain one valid sliding window.
#A map stores the latest index of each character. If s[right] previously appeared inside the current window, left can jump directly after that occurrence. If the saved index lies before left, it belongs to an old window and can be ignored.
#This keeps both pointers moving only forward.

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

