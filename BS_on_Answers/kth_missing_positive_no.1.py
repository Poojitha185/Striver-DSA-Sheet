#Time Complexity: O(logn), used for typical binary search

#Space Complexity: O(1), no extra space used

#We cannot apply binary search on the answer space here as we cannot assure which missing number has the possibility of being the kth missing number. That is why, we will do something different here. We will try to find the closest neighbors (i.e. Present in the array) for the kth missing number by counting the number of missing numbers for each element in the given array.

#using binary search

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