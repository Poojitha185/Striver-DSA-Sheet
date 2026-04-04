#TC:O(n**2)
#SC=O(1), as we are not using any extra space to store the elements and modifying the original array in place.
def missing_number(arr,n):
    for i in range(1,n+1):  #tc:o(n)
        if i not in arr:  #tc:o(n)
           return i

arr=list(map(int,input("enter the first sorted arary: ").split(',')))
n=len(arr)
print("The missing number in the array is",missing_number(arr,n+1))