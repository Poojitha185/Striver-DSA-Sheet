def kth_missing_number(arr,n,k):
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        missing=arr[mid]-(mid+1)
        if missing<k:
            low=mid+1
        else:
            high=mid-1
    return (high+1+k)            # or return(low+k),because low=high+1 after we done with the binary serach in a arr where low ended after high
arr = list(map(int, input("Enter the array: ").split(',')))
k = int(input("Enter the value of k: "))
n=len(arr)
print("The kth missing positive number is:", kth_missing_number(arr,n,k))