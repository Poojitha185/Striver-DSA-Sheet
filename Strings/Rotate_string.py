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
