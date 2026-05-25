#Time Complexity: O(n * max(a[])), since for each possible speed we go through all the piles.
#Space Complexity: O(1), since the algorithm does not use any additional space or data structures.

import math
from math import ceil
def min_integer(arr,n,h):
    reqtime=0
    for i in range(1,max(arr)+1):  #bcz its starting from 1
        reqtime=totaltime(arr,i)
        if reqtime<=h:
         return i
def totaltime(arr,i):
    totaltime=0
    for j in arr:
      totaltime+=ceil(j/i)       #ceil() means ceiling function.It rounds a number up to the nearest integer
    return totaltime
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
h=int(input("enter the hours: "))
print("The minimum integer is:",min_integer(arr,n,h))
