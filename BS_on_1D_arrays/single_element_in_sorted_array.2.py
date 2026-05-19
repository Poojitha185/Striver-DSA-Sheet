def single_element(arr,n):
    ans=0
    for i in range(n):
        ans^=arr[i]
    return ans
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The single element in the array is:",single_element(arr,n))