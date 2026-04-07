def longest_subarray_sum(arr,n,k):
    right=0
    left=0
    len=0
    sum=arr[0]
    while(right<n):
        while(left<=right and sum>k):
            sum=sum-arr[left]
            left+=1
        if sum==k:
            len=max(len,right-left+1)
        right+=1
        if right<n:
            sum+=arr[right]
    return len
arr=arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
k=int(input("enter the sum(k) value: "))
print("The length of the longest subarray:",longest_subarray_sum(arr,n,k))