#The naive method checks every speed, which is slow if the piles are large. But the possible answer space (from 1 to the maximum pile size) is sorted, meaning if a certain speed works, then all higher speeds will also work. This allows us to apply Binary Search on the answer space to efficiently find the minimum speed at which Koko can finish the bananas within the given hours.
#Time Complexity: O(N*log(max(a[]))), we apply binary search on our search space to reduce it into half at every step.
#Space Complexity: O(1), since the algorithm does not use any additional space or data structures.

import math
from math import ceil

def minEatingSpeed(arr,n,h):
   low,high=1,max(arr)
   while low<=high:
      mid=(low+high)//2
      reqtime=totaltime(arr,mid)
      if reqtime<=h:
         high=mid-1
      else:
         low=mid+1
   return low
def totaltime(arr,i):
    totaltime=0
    for j in arr:
      totaltime+=ceil(j/i)       #ceil() means ceiling function.It rounds a number up to the nearest integer
    return totaltime
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
h=int(input("enter the hours: "))
print("The minimum integer is:",minEatingSpeed(arr,n,h))