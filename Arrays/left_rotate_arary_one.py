#TC:O(N),  as we are iterating through the array once to perform the left rotation.
#SC:O(1) bcz we are using a constant amount of extra space to store the first element of the array and not using extra space for new arary 
#we are using given array in alogrithm to modify so sc is o(n) but when its comes to extra space sc is o(1)
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
