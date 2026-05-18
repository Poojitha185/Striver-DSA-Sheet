def rotations_count(arr,n):
    low,high=0,n-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]>arr[high]:
            low=mid+1
        else:
            high=mid
    return low
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The number of times the array is rotated is:",rotations_count(arr,n))