#Time Complexity: O(log N), we reduce the search space to half at every step using binary search.
#Space Complexity: O(1), constant additional space is used.
#we know that if current element is greater than its left neighbour, we are in the left half and if our current element is greater than its right neighbour then we are in the right half. If we know the half that we are in currently, we can eliminate it to find our peak element.
#using binary search

def peak_element(arr,n):
    low,high=0,n-1
    while low<high:
        mid=(low+high)//2
        if arr[mid]>arr[mid+1]:
            high=mid
        else:
            low=mid+1
    return low
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The index of the peak element is:",peak_element(arr,n))