def min_days(arr,n,d):
    low,high=max(arr),sum(arr)
    while low<= high:
        mid=(low+high)//2
        reqdays=totaldays(arr,mid)
        if reqdays<=d:
            high=mid-1
        else:
            low=mid+1
    return low
def totaldays(arr,capacity):
    days=1
    load=0
    for j in arr:
        if((load+j)>capacity):
            days+=1
            load=j
        else:
            load+=j
    return days
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
d=int(input("enter the days: "))
print("The minimum days required to ship all packages is:",min_days(arr,n,d))