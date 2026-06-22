def anagram_check(s1,s2):
    if len(s1)!=len(s2):
        return False
    freq=[0]*26                                 #freq array of size 26 and all elements are initialized to 0.
    for i in s1:
        freq[ord(i)-ord('a')]+=1                #subtracting 'a' from the character gives us the index in the frequency array corresponding to that character
    for j in s2:
        freq[ord(j)-ord('a')]-=1
    for count in freq:
        if count!=0:
            return False
    return True
s1=input("enter thr first string: ")
s2=input("enter the second string: ")
print("does both the strings anagram of each other: ",anagram_check(s1,s2))
