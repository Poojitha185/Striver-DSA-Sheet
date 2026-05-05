#TC: O(N), where N is the size of the array. This is because we are iterating through the array once to find the target element.
#SC: O(1), as we are using a constant amount of space for variables, regardless of the input size.
def search_X(arr,n,target):
    for i in range(n):
        if arr[i]==target:
          return i
    return -1
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
target=int(input("enter the target: "))
print("the target is found at index: ",search_X(arr,n,target))
