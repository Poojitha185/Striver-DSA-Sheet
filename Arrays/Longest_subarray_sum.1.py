#Time Complexity: O(N), where N is the size of the array. The algorithm traverses the array once with two pointers, making it linear in time complexity.
#Space Complexity: O(1), as it uses a constant amount of space.
#using two pointers approach 
#It is optimal solution for array contain zeros and positives
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