#Time Complexity: O(N^2), where N is the size of the array. This is because we have two nested loops: one for the starting index and one for the ending index of the subarray.

#Space Complexity: O(1), as we are using a constant amount of space for variables, regardless of the input size.

def maximum_subarray_sum(arr,n):
    maxi=arr[0]
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            maxi=max(maxi,sum)
    return maxi
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The maximum subarray sum is: ",maximum_subarray_sum(arr,n))
        