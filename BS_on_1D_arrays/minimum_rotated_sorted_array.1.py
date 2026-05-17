#Time Complexity: O(logN), at every step the search space is reduced to half using binary search.
#Space Complexity: O(1), constant additonal space is used.
#using binary search approach
def minimum_rotated_sorted_array(arr,n):
    ans = float('inf')  #inf=infinity,We use this often when finding minimum element,minimum distance,smallest value and similarily for maximum element we use -inf.
    low,high=0,n-1
    while(low<=high):
        mid=(low+high)//2
        if arr[low]<=arr[high]:
            ans=min(ans,arr[low])
            break
        if arr[low]<=arr[mid]:
            ans=min(ans,arr[low])
            low=mid+1
        else:
            ans=min(ans,arr[mid])
            high=mid-1
    return ans
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The minimum element in the array is:",minimum_rotated_sorted_array(arr,n))

