#Time Complexity: O(n),We scan the entire array once to find the smallest element, where n is the size of the array.

#Space Complexity: O(1),We only use a few extra variables to store the minimum value and its index, so the extra space used is constant.

#we simply search for the smallest element in the array because it’s the point where the rotation happened its index directly tells us the rotation count

#using linear search approach to find the index of the minimum element which is also the number of times the array is rotated.

def no_of_rotations(arr,n):
    min=arr[0]
    for i in range(n):
        if arr[i]<min:
            min=arr[i]
    return arr.index(min)
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The number of times the array is rotated is:",no_of_rotations(arr,n))