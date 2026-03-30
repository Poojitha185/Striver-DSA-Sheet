def is_sorted(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                return False
    return True
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print(is_sorted(arr,n))        