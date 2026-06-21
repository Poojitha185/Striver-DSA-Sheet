def rotate_string(s,goal):
    if len(s)!=len(goal):
        return False
    double_s=s+s
    return goal in double_s
s=input("enter the first string: ")
goal=input("enter the second string: ")
print("The two strings are rotations of each other:",rotate_string(s,goal))

