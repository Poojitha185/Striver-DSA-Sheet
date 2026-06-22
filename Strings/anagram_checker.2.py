#Time Complexity: O(N), where N is the length of the strings. Each string is traversed once, and the frequency array is checked in constant time (26 iterations).

#Space Complexity: O(1), as a fixed-size array of 26 elements is used regardless of the input size.

#Initialize a frequency array of size 26 (for all uppercase English letters) and set all elements to 0.

#Traverse the first string and increment the frequency of each character.

#Traverse the second string and decrement the frequency of each character.

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
