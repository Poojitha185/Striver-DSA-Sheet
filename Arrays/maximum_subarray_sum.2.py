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