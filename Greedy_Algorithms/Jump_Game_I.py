#Time Complexity: O(n), because the array is scanned once.
#Space Complexity: O(1), because constant space is used.

def can_jump(arr):
    max_jump=0
    for i in range(len(arr)):
        if i>max_jump:
            return False
        max_jump=max(max_jump,i+arr[i])
        if max_jump>=len(arr)-1:
            return True
    return True
arr=list(map(int,input("Enter the list of maximum jump lengths: ").split(",")))
print(can_jump(arr))