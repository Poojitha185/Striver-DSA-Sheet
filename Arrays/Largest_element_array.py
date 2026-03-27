#Time Complexity: O(N), where N is the size of the array, as we are iterating through the array once.
#Space Complexity: O(1), as we are using a constant
def largest_element(arr,n):
    large=arr[0]
    for i in range(n):
        if arr[i]>large:
         large=arr[i]
    return large
arr=arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print("the largest element of an array: ",largest_element(arr,n))

