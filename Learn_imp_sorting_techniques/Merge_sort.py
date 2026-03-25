#Time Complexity: O(N*logN), merging two arrays take linear time and array is recursively divided into halves (logN times).
#Space Complexity: O(N), we use a temporary array to store elements in sorted order.
#“In index-based merge sort, we copy back to the original array because recursion operates on subarray ranges, not separate arrays.”
def merge(arr,low,mid,high):
    left=low
    right=mid+1
    temp=[]
    while(left<=mid and right<=high):
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left=left+1
        else:
            temp.append(arr[right])
            right=right+1
    while(left<=mid):
          temp.append(arr[left])
          left=left+1
    while(right<=high):
         temp.append(arr[right])
         right=right+1
    for i in range(low, high + 1):    #We reassign to arr because recursion depends on original arraywe are sorting subarrays using indicestemp is just temporary storage
            arr[i] = temp[i - low]    # temp is a new small array starting at 0
                                      # arr is a big array starting at low, so we need to do i-low to get the correct index in temp
def merge_sort(arr,low,high):
    if low>=high:
        return 
    mid=(low+high)//2
    merge_sort(arr,low,mid)
    merge_sort(arr,mid+1,high)
    merge(arr,low,mid,high)
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
merge_sort(arr,0,n-1)
print(arr)