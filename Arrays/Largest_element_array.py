#Time Complexity: O(N log N), where N is the size of the array, as we are sorting the array.
#Space Complexity: O(1), as we are using a constant
def large_element(arr,n):
    arr.sort()
    return arr[n-1]    #or return arr[-1]
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print("the largest element of an array: ",large_element(arr,n))