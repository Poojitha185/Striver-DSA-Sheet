#TC~O(N*N)
#SC:O(1), as we are not using any extra space.
def longest_subarray_sum_k(arr,n,k):
    length=0
    #creating all possible subarrays and calculating their sum and comparing with k
    for i in range(n):               #tc:o(n) as we are iterating through the array once
        sum=0             
        for j in range(i,n):           #tc~o(n) as we are iterating through the array once for each element
            sum=sum+arr[j]             
            if sum==k:
             length=max(length,j-i+1) 
    return length
arr=arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
k=int(input("enter the sum(k) value: "))
print("The length of the longest subarray:",longest_subarray_sum_k(arr,n,k))
               