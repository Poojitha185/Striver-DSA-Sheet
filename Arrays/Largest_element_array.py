def largest_element(arr,n):
    large=arr[0]
    for i in range(n):
        if arr[i]>large:
         large=arr[i]
    return large
arr=arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print("the largest element of an array: ",largest_element(arr,n))

