#Anagram: An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

#Time Complexity: O(N log N), where N is the length of the strings. This is due to the sorting step performed on both strings.

#Space Complexity: O(1), as the sorting is done in-place and no extra space proportional to input size is used (excluding the input strings themselves).

#First, check if the lengths of both strings are equal. If not, they can't be anagrams and return false immediately.

#If the lengths match, sort both strings using a built-in sorting algorithm.

#Once sorted, iterate through each character of both strings and compare them one by one.

def anagram_checker(s1,s2):
    if len(s1)!=len(s2):
        return False
    if sorted(s1)==sorted(s2):
        return True
    return False
s1=input("enter thr first string: ")
s2=input("enter the second string: ")
print("does both the strings anagram of each other: ",anagram_checker(s1,s2))