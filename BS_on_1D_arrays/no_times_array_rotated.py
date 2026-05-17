def no_of_rotations(arr,n):
    min=arr[0]
    for i in range(n):
        if arr[i]<min:
            min=arr[i]
    return arr.index(min)
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The number of times the array is rotated is:",no_of_rotations(arr,n))