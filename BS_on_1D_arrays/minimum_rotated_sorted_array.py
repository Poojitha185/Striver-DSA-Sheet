def minimum(arr,n):
    min=arr[0]
    for i in range(n):
        if arr[i]<min:
            min=arr[i]
    return min
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("the minimum element in the array is:",minimum(arr,n))
