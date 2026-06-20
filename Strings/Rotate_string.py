#Time Complexity: O(N^2) since generating N rotations and each comparison takes O(N) time.

#Space Complexity: O(N) for the space needed to store each rotated string.

#Start by generating all possible left rotations of the original string using substring slicing and concatenation.

#For each rotated version of the string, compare it with the target (goal) string.

def rotate_string(s,goal):
    if len(s)!=len(goal):
        return False
    for i in range(len(s)):
        rotated=s[i:]+s[:i]
        if rotated==goal:
            return True
    return False
s=input("enter the first string: ")
goal=input("enter the second string: ")
print("The two strings are rotations of each other:",rotate_string(s,goal))
