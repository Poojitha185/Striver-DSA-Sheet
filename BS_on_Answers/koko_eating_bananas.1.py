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