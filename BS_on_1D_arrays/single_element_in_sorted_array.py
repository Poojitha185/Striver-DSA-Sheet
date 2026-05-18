#Time Complexity = O(n²)
#Space Complexity = O(1)

def single_element(arr,n):
    for i in range(n):         #tc:o(n)
        k=arr.count(arr[i])    #tc:o(n)
        if k==1:
         return arr[i]
    return 0
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("the single element in the array is:",single_element(arr,n))
    