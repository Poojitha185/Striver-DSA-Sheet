def sort_0_1_2(arr,n):
    low,mid,high=0,0,n-1
    while(mid<high):
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            mid=mid+1
            low=low+1
        elif arr[mid]==1:
            mid=mid+1
        elif arr[mid]==2:
            arr[mid],arr[high]=arr[high],arr[mid]
            high=high-1
    return arr
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print(sort_0_1_2(arr,n))    