#Time Complexity: O(1) O(log(max(arr[])-min(arr[])+1) * N), where {max(arr[]) -> maximum element of the array, min(arr[]) -> minimum element of the array, N = size of the array}.

#Space Complexity : O(h)O(1) as we are not using any extra space to solve this problem.

#using binary search to find the minimum day required to make m bouquets from the given array of blooming days of flowers. The binary search will help us efficiently narrow down the potential days to check for bouquet formation.

#Eliminate the halves based on the value returned by possible(): We will pass the potential answer, represented by the variable 'mid' (which corresponds to a specific day), to the 'possible()' function.
#If possible() returns true: On satisfying this condition, we can conclude that the number ‘mid’ is one of our possible answers. But we want the minimum number. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).
#Otherwise, the value mid is smaller than the number we want. This means the numbers greater than ‘mid’ should be considered and the right half of ‘mid’ consists of such numbers. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).
#Finally, outside the loop, we will return the value of low as the pointer will be pointing to the answer.

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
    if(m*k>n):                         #If m*k > arr.size: This means we have insufficient flowers. So, it is impossible to make m bouquets and we will return -1.
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