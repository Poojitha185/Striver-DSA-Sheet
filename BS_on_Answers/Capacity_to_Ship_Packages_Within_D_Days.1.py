#Time Complexity: O(N * log(S)), where N is number of packages and S is the search space (sum_weights - max_weight). Each binary search step takes O(N), repeated O(log S) times.
#Space Complexity: O(1), constant extra space used.
# The capacity must be at least the heaviest package because you can’t split a package. 
# At the same time, the capacity can be at most the sum of all packages (if you ship everything in one day). So the answer lies between these two extremes.
# Using binary search on this range lets us efficiently find the smallest capacity that works. For each candidate capacity, we check if it’s possible to ship all packages within the given days by greedily accumulating package weights until we reach capacity, then moving to the next day.
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