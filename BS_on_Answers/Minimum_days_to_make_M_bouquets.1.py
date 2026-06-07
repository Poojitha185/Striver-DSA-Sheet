def possible(arr,n,i,m,k):
    count=0
    no_of_bou=0
    for j in range(n):
        if arr[j]<=i:
            count+=1
        else:
            no_of_bou+=(count//k)
            count=0
    no_of_bou+=(count//k)            #To account for the last bouquet if the last flowers are blooming before or on day i
    if no_of_bou>=m:
        return True
    else:
        return False
def minimum_day(arr,n,m,k):
    if(m*k>n):
        return -1
    low,high=min(arr),max(arr)
    while low<=high:
        mid=(low+high)//2
        if (possible(arr,n,mid,m,k)==True):
            high=mid-1
        else:
            low=mid+1
    return low
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
m=int(input("enter the number of bouquets: "))
k=int(input("enter the number of flowers in each bouquet: "))
print("The minimum day required to make bouquets is:",minimum_day(arr,n,m,k))