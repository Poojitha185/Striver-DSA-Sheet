def single_element(arr,n):
    for i in range(n):
        k=arr.count(arr[i])
        if k==1:
         return arr[i]
    return 0
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("the single element in the array is:",single_element(arr,n))
    