#Time Complexity: O(N*logN), merging two arrays take linear time and array is recursively divided into halves (logN times).
#Space Complexity: O(N), we use a temporary array to store elements in sorted order.
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
    for i in range(low, high + 1):
            arr[i] = temp[i - low]

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