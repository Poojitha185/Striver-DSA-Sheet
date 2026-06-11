#Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.

#Space Complexity:  O(1) as we are not using any extra space to solve this problem.

#We perform Binary Search:
#We try a middle value of pages per student.
#We check how many students would be required if no student gets more than that value.
#If it takes more students than allowed, that value is too low, so we try a higher one.
#If it fits within the allowed number of students, we store it and try a smaller one to find an even better option.

def ispossible(arr,j,n,k):
    d=1
    l=0
    for i in range(n):
        if(arr[i]>j):
            return False
        if (l+arr[i]>j):
            d+=1
            l=arr[i]     #assign the new value of arr to l when we start with new subarray
        else:
            l+=arr[i]
    if (d>k):
        return False
    return True
def split_arrays(arr,n,k):
    if k>n:
        return -1
    low=max(arr)
    high=sum(arr)            
    while(low<=high):
        mid=(low+high)//2         
        if(ispossible(arr,mid,n,k)==True):
            high=mid-1
        else:
            low=mid+1
    return low
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
k=int(input("enter the number of consecutive subarrays:"))
print("The largest sum among the subarrays:",split_arrays(arr,n,k))