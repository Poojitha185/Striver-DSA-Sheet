def left_rotate_one(arr,n):
    temp=arr[0]
    for i in range(1,n):
        arr[i-1]=arr[i]
    arr[-1]=temp
    return arr
arr=arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print("array before rotating by one: ",arr)
print("array after rotating by one: ",left_rotate_one(arr,n))
