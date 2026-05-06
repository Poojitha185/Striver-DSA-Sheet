#Time Complexity: O(logn), used for typical binary search
#Space Complexity: O(1), no extra space used
#using binary search approach
def lower_bound(arr,x,n):
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>=x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=list(map(int,input("enter the array: ").split(',')))
x=int(input("enter the target: "))
n=len(arr)
print("the target is found at index:",lower_bound(arr,x,n))
