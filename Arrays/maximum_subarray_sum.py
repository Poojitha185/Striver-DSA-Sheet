
#Time Complexity: O(N^3), where N is the size of the array. This is because we have three nested loops: one for the starting index, one for the ending index, and one for calculating the sum of the subarray.

#Space Complexity: O(1), as we are using a constant amount of space for variables, regardless of the input size.

def maximum_subarray_sum(arr,n):
    maxi=arr[0]
    for i in range(n):
        for j in range(i,n):
            sum=0
            for k in range(i,j+1):
                sum+=arr[k]
            maxi=max(maxi,sum)
    return maxi
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The maximum subarray sum is: ",maximum_subarray_sum(arr,n))