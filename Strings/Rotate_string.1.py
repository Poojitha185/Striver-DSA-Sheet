#Time Complexity: O(N), because checking for a substring in s + s is linear in time.

#Space Complexity: O(N) for the space needed to store the concatenated string s + s.

#This code works for any number roations

#Double the original string by joining it with itself, creating a new string like s + s.

#Look for the target string goalinside this new doubled string.

def rotate_string(s,goal):
    if len(s)!=len(goal):
        return False
    double_s=s+s
    return goal in double_s
s=input("enter the first string: ")
goal=input("enter the second string: ")
print("The two strings are rotations of each other:",rotate_string(s,goal))

