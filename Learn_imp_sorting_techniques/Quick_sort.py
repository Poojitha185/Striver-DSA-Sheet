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