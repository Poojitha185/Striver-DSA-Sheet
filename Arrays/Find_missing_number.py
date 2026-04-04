def missing_number(arr,n):
    for i in range(1,n+1):
        if i not in arr:
           return i

arr=list(map(int,input("enter the first sorted arary: ").split(',')))
n=len(arr)
print("The missing number in the array is",missing_number(arr,n+1))