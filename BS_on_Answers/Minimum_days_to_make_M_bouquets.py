#Time Complexity: O((max(arr[])-min(arr[])+1) * N), where {max(arr[]) -> maximum element of the array, min(arr[]) -> minimum element of the array, N = size of the array}.
#Space Complexity : O(1) as we are not using any extra space to solve this problem.

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
    for i in range(min(arr),max(arr)):
        if(possible(arr,n,i,m,k)==True):
         return i
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
m=int(input("enter the number of bouquets: "))
k=int(input("enter the number of flowers in each bouquet: "))
print("The minimum day required to make bouquets is:",minimum_day(arr,n,m,k))