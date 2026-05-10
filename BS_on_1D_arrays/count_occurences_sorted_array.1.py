def first_occurence(arr,n,x):
    first=-1
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            first=mid
            high=mid-1
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return first
def last_occurence(arr,n,target):
    last=-1
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            low=mid+1
            last=mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return last
def firstandlast(arr,n,x):
 first=first_occurence(arr,n,x)
 if first==-1:
     return (-1,-1)
 last=last_occurence(arr,n,x)
 return first,last
def count_occurences(arr,n,x):
 first,last=firstandlast(arr,n,x)
 if first==-1:
     return 0
 else:
     return(last-first+1)
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
target=int(input("enter the target: "))
print("the target is found",count_occurences(arr,n,target),"times in the array")
    
