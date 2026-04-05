#Time Complexity: O(N), since we scan the array once.
#Space Complexity: O(1), as only constant extra variables are used.
def maximum_consecutive_ones(arr):
    cnt=0
    maxi=0
    for i in range(len(arr)):
        if arr[i]==1:
            cnt=cnt+1
        else:
            cnt=0
        maxi= max(maxi,cnt)
    return maxi
arr=list(map(int,input("enter the array: ").split(',')))
print("The maximum consecutive ones:",maximum_consecutive_ones(arr))
