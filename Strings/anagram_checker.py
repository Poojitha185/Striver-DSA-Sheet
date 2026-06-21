#TC:O(N^2)
#SC:O(1)
def anagram_check(s1,s2):
    if len(s1)!=len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] not in s2:
          return False
    return True
s1=input("enter thr first string: ")
s2=input("enter the second string: ")
print("does both the strings anagram of each other: ",anagram_check(s1,s2))