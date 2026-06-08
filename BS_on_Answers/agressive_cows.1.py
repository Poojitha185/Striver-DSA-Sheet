#Time Complexity: O(NlogN) + O(N * log(max(stalls[])-min(stalls[]))), where N = size of the array, max(stalls[]) = maximum element in stalls[] array, min(stalls[]) = minimum element in stalls[] array.

#Space Complexity: O(1) as we are not using any extra space to solve this problem.

#Use Binary Search: Repeat the process until the search range is exhausted:
#Pick the middle distance: Test this distance as a possible answer.
#Check if it works:
#If it works: Try to increase the distance to see if a larger one is possible.
#If it doesn’t work: Decrease the distance and test smaller ones.

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