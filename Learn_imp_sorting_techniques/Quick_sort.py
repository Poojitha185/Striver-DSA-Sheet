#Time Complexity: O(N*logN), At each step, we divide the whole array, for that we take logN time and n steps are taken for the partitioning. In worst case i.e. when our pivot is always the greatest or the smallest element of the array, the time complexity can be O(N^2).
#Space Complexity: O(N), auxiliary stack space.

def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while(i<j):
        while(arr[i]<=pivot and i<=high-1):
            i=i+1
        while(arr[j]>pivot and j>=low+1):
            j=j-1
        if (i<j):
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j


def quick_sort(arr,low,high):
    if (low<high):
        partition_index=partition(arr,low,high)
        quick_sort(arr,low,partition_index-1)
        quick_sort(arr,partition_index+1,high)
arr=list(map(int,input("enter the arary: ").split(',')))
quick_sort(arr,0,len(arr)-1)
print("After the quick sort the array: ",arr)