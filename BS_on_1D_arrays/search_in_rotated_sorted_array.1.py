def search(arr,n,target):
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=target<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<target<=arr[high]:
                low=high+1
            else:
                high=mid-1
    return -1
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
target=int(input("enter the target: "))
print("the target is found at index:",search(arr,n,target))