#Time Complexity: O(n), We are performing a constant number of linear operations copying `d` elements and shifting up to `n-d` elements.
#Space Complexity: O(d) ,A temporary array of size `d` is used to store either the first `d` or last `d` elements depending on the direction of rotation.
def left_rotate_D(arr,n,d):
    d=d%n
    temp=[]
    for i in range(d):
      temp.append(arr[i])
    for i in range(d,n):
        arr[i-d]=arr[i]
    for i in range(n-d,n):
        arr[i]=temp[i-(n-d)]      #i-(n-d) or initialise j=0 and increment after each insert
    return arr
arr=arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
d=int(input("enter no of places to rotate: " ))
print("array before rotating by one: ",arr)
print("array after rotating by one: ",left_rotate_D(arr,n,d))