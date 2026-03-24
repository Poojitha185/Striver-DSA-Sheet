#Time Complexity: O(N2), (where N = size of the array), for the worst, and average cases.
#Space Complexity: O(1).
def bubble_sort(n,arr):
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if arr[j]>arr[j+1]:
              arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print("Before using bubble sort the arary: ",arr)
print("After the bubble sort the array: ",bubble_sort(n,arr))