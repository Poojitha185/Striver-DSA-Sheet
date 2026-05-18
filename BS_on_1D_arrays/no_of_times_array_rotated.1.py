def rotation_count(arr,n):
    for i in range(n-1):
        if arr[i+1]>arr[i]:
            return i+1
    return 0
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The number of times the array is rotated is:",rotation_count(arr,n))
