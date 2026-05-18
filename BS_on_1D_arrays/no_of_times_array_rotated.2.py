#Time Complexity: O(log n),The binary search halves the search space each iteration, where n is the size of the array.

#Space Complexity: O(1),Only a few variables are used regardless of input size, so constant extra space.

#using binary search

def rotations_count(arr,n):
    low,high=0,n-1
    while low<high:     #we use low<high not low<=high because for low<=high then loop runs one extra time unnecessarily.
        mid=(low+high)//2
        if arr[mid]>arr[high]:
            low=mid+1
        else:
            high=mid
    return low         #when low==high then the index of low will be the no of rotations
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The number of times the array is rotated is:",rotations_count(arr,n))