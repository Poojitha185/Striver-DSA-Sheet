def longest_subarray_sum_k(arr,n,k):
    length=0
    for i in range(n):
        for j in range(i,n):
           sum=0
           for l in range(i,j+1):
               sum=sum+arr[l]
           if sum==k:
            length=max(length,j-i+1) 
    return length
arr=arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
k=int(input("enter the sum(k) value: "))
print("The length of the longest subarray:",longest_subarray_sum_k(arr,n,k))
               