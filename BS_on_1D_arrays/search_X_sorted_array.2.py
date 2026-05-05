def binary_search_recursive(arr,low,high,target,n):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif target>arr[mid]:
        return binary_search_recursive(arr,mid+1,high,target,n)
    else:
        return binary_search_recursive(arr,low,mid-1,target,n)
arr=list(map(int,input("enter the array: ").split(',')))
target=int(input("enter the target: "))
n=len(arr)
print("the target is found at index:",binary_search_recursive(arr,0,n-1,target,n))
