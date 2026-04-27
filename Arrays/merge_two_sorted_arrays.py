#Time Complexity: O(N+M), we traverse both the arrays exactly once.
#Space Complexity: O(1), constant extra space is used to store pointers.
#using Three pointers , we start from the end of both arrays and compare the elements. We place the larger element at the end of the first array and move the pointers accordingly. This way, we can merge the two sorted arrays in place without using any extra space.
def merge_two_sorted_arrays(arr1,arr2,m,n):
    i=m-1
    j=n-1
    k=m+n-1
    while i>=0 and j>=0:
        if arr1[i]>arr2[j]:
            arr1[k]=arr1[i]
            i=i-1
        else:
            arr1[k]=arr2[j]
            j=j-1
        k=k-1
    while j>=0:
        arr1[k]=arr2[j]
        k=k-1
        j=j-1
    return arr1
arr1=list(map(int,input("enter the first sorted array: ").split(',')))
arr2=list(map(int,input("enter the second sorted array: ").split(',')))
m=len(arr1)
n=len(arr2)
arr1.extend([0] * n)
print("array after merging two sorted arrays: ",merge_two_sorted_arrays(arr1,arr2,m,n))