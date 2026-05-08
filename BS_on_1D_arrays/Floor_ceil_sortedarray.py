#Time Complexity:O(logN), where N = size of the given array. We are using the Binary Search algorithm

#Space Complexity: O(1). No extra space used

def floor(arr,n,k):
    low=0
    high=n-1
    floor =-1
    while low <= high:
        mid=(low+high)//2
        if arr[mid]<=k:
            floor=arr[mid]
            low=mid+1
        else:
            high=mid-1
    return floor
def ceil(arr,n,k):
    low=0
    high=n-1
    ceil=-1
    while low <= high:
        mid=(low+high)//2
        if arr[mid]>=k:
            ceil=arr[mid]
            high=mid-1
        else:
            low=mid+1
    return ceil
arr=list(map(int,input("enter the array: ").split(',')))
k=int(input("enter the target: "))
n=len(arr)
floor,ceil=floor(arr,n,k),ceil(arr,n,k)
print("the floor and ceil of the target is found at index:",floor,ceil)
