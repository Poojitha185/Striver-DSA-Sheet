def search(arr,n,target):
    for i in range(n):
        if arr[i]==target:
            return True
    return False
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
target=int(input("enter the target: "))
print(search(arr,n,target))