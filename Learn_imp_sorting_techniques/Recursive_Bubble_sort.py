#Time Complexity: O(N2), (where N = size of the array), for the worst, and average cases.
#Space Complexity: O(N) auxiliary stack space.
def recursive_bubble_sort(arr,n):
    if n==0:
        return
    for j in range(0,n-1):
            if arr[j]>arr[j+1]:
              arr[j],arr[j+1]=arr[j+1],arr[j]
    recursive_bubble_sort(arr,n-1)
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print("Before using bubble sort the arary: ",arr)
recursive_bubble_sort(arr,n)
print("After the bubble sort the array: ",arr)