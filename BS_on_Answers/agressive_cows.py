#Time Complexity: O(NlogN) + O(N *(max(stalls[])-min(stalls[]))), where N = size of the array, max(stalls[]) = maximum element in stalls[] array, min(stalls[]) = minimum element in stalls[] array.

#Space Complexity: O(1) as we are not using any extra space to solve this problem.

#The basic idea is to test every possible distance between 1 and the difference between the farthest and nearest stalls. The largest distance for which canWePlace() returns true will be our answer.

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
      ans=0
      maxdis=arr[n-1]-arr[0]
      for d in range(1,maxdis+1):
       if (canplace(arr,d,cows,n)==True):
            ans=d
      return ans
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
cows=int(input("enter the number of cows: "))
print("The largest minimum distance is:",agressivecows(arr,cows,n))
                 