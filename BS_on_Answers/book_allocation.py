def ispossible(arr,j,n,s):
    no_of_students=1
    pages=0
    for i in range(n):
        if(arr[i]>j):
            return False
        if (pages+arr[i]>j):
            no_of_students+=1
            pages+=arr[i]
        else:
            pages+=arr[i]
    if (no_of_students>s):
        return False
    return True
def allocation(arr,n,s):
    if s>n:
        return -1
    low=min(arr)
    high=sum(arr)
    for j in range(low,high+1):
        if(ispossible(arr,j,n,s)==True):
            return j
    return -1
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
s=int(input("enter the number of students: "))
print("The minimum number of pages is:",allocation(arr,n,s))