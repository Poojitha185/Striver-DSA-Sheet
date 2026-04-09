#TC:O(nlogn) for sorting the array and O(n) for iterating through the array with two pointers, resulting in an overall time complexity of O(nlogn).
#SC:O(1), as we are not using any extra space to store the elements and modifying the original array in place.
#If we cares about time → use hashing
#If we cares about space → two-pointer is better
#Two pointer approach
def two_sum(arr,n,target):
    left=0
    right=n-1
    arr.sort()
    while(left<right):    
        if arr[left]+arr[right]==target:
            return "YES"
        elif arr[left]+arr[right]<target:
            left=left+1
        else:
            right=right-1
    return "NO"
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
target=int(input("enter the target sum: "))
print(two_sum(arr,n,target))