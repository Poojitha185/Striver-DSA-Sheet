#Time Complexity: O(N2), (where N = size of the array), for the worst, and average cases.
#Space Complexity: O(N) auxiliary stack space.
def recursive_insertion_sort(arr,n,k):
    if k==n:
        return
    j=k
    while(j>0 and (arr[j-1]>arr[j])):
         arr[j-1],arr[j]=arr[j],arr[j-1]
         j=j-1
    recursive_insertion_sort(arr,n,k+1)
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print("Before using insertion sort the arary: ",arr)
recursive_insertion_sort(arr,n,0)
print("After the insertion sort the array: ",arr)