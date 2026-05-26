#Time Complexity: O((sum_weights - max_weight) * N), where N is the number of packages. For each capacity between max weight and total sum, we simulate shipping over N packages.

#Space Complexity: O(1), only constant extra space is used.

#A brute force way is to check every capacity starting from the maximum single package weight (since capacity can't be less than the heaviest package) up to the sum of all package weights (which guarantees all packages shipped in one day). For each capacity, simulate the shipping process day by day. The smallest capacity that ships all packages in ≤ d days is the answer.

def min_days(arr,n,d):
    for i in range(max(arr),sum(arr)+1):
        reqdays=totaldays(arr,i)
        if reqdays <= d:
            return i
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
