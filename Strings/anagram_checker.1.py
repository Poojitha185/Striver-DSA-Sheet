def anagram_checker(s1,s2):
    if len(s1)!=len(s2):
        return False
    if sorted(s1)==sorted(s2):
        return True
    return False
s1=input("enter thr first string: ")
s2=input("enter the second string: ")
print("does both the strings anagram of each other: ",anagram_checker(s1,s2))