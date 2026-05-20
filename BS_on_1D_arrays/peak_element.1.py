def peak_element(arr,n):
    low,high=0,n-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]>arr[mid+1]:
            high=mid
        else:
            low=mid+1
    return low
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The index of the peak element is:",peak_element(arr,n))