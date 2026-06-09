def ispossible(arr,j,n,s):
    no_of_students=1
    pages=0
    for i in range(n):
        if(arr[i]>j):
            return False
        if (pages+arr[i]>j):
            no_of_students+=1
            pages=arr[i]                 #assign the new value of arr to pages when we start to assign pages for new students
        else:
            pages+=arr[i]
    if (no_of_students>s):
        return False
    return True
def allocation(arr,n,s):
    if s>n:
        return -1
    low=max(arr)
    high=sum(arr)
    while(low<=high):
        mid=(low+high)//2
        if(ispossible(arr,mid,n,s)==True):
            high=mid-1
        else:
            low=mid+1
    return low
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
s=int(input("enter the number of students: "))
print("The minimum number of pages is:",allocation(arr,n,s))