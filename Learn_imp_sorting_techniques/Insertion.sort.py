#Time Complexity: O(n^2), where n is the number of elements in the array. This is because, in the worst case, we may have to compare each element with all the previous elements.
#Space Complexity: O(1), as we are sorting the array in place and not using any additional data structures that grow with input size.
def insertion_sort(n,arr):
    for i in range(0,n):
        j=i
        while(j>0 and (arr[j-1]>arr[j])):
         arr[j-1],arr[j]=arr[j],arr[j-1]
         j=j-1
    return arr
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print("Before using insertion sort the arary: ",arr)
print("After the insertion sort the array: ",insertion_sort(n,arr))