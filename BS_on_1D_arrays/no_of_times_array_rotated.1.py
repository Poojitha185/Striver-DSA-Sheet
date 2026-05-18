#Time Complexity: O(n),We traverse the array once to find the rotation point, where n is the size of the array.

#Space Complexity: O(1),Only a few extra variables are used regardless of input size, so constant space.

def rotation_count(arr,n):
    for i in range(n-1):
        if arr[i+1]<arr[i]:
            return i+1
    return 0
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The number of times the array is rotated is:",rotation_count(arr,n))

