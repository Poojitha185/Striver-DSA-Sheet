#Time Complexity: O(n), because the array is scanned once.
#Space Complexity: O(1), because constant space is used.

#Start with farthest = 0 because at the beginning only index 0 is surely reachable.
#Traverse the array from left to right because reachability grows forward from the starting index.
#Before using index i, check whether i > farthest. This check is needed because an unreachable index cannot be used to make another jump.
#If index i is reachable, update farthest with max(farthest, i + nums[i]). This keeps the best reachable boundary found so far.
#If farthest becomes greater than or equal to the last index, return true because reaching or crossing the last index is enough.
#If the loop finishes without getting stuck, return true because every needed position was reachable.

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