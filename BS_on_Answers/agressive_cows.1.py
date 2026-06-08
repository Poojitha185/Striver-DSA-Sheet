def canplace(arr,d,cows,n):
    count=1
    lastcow=arr[0]
    for i in range(n):
           if(arr[i]-lastcow>=d):
                 count+=1
                 lastcow=arr[i]
           if count>=cows:
                  return True
    return False
def agressivecows(arr,cows,n):
      arr.sort()
      low,high=1,arr[n-1]-arr[0]
      while(low<=high):
            mid=(low+high)//2
            if(canplace(arr,mid,cows,n)==True):
                  low=mid+1
            else:
                  high=mid-1
      return high
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
cows=int(input("enter the number of cows: "))
print("The largest minimum distance is:",agressivecows(arr,cows,n))