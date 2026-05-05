def search_X(arr,n,target):
    for i in range(n):
        if arr[i]==target:
          return i
    return -1
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
target=int(input("enter the target: "))
print("the target is found at index: ",search_X(arr,n,target))
