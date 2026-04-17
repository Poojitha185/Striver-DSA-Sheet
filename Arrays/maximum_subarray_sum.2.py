#Time Complexity: O(n), where n is the number of elements in the array. We traverse the array only once.

#Space Complexity: O(1). We use a constant amount of space for variables.

#maximum subarray sum is entire array sum but when we find sum of array it will give wrong answer when array contain negative numbers so we will reset sum to 0 when it becomes negative because negative sum will decrease the overall sum of the subarray. This way, we can ensure that we are always considering the maximum possible sum for the subarray.

def maximum_subarray(arr,n):
     sum=0
     maxi=arr[0]
     for i in range(n):
          sum+=arr[i]
          maxi=max(maxi,sum)
          if sum<0:
            sum=0
     return maxi
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The maximum subarray sum is:",maximum_subarray(arr,n))