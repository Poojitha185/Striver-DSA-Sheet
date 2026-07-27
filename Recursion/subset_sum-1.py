
#We can solve this more cleanly using recursion without generating all bitmasks. Start from index 0, maintain a running sum, and at each index, make two recursive calls—one including the current element and one excluding it. When we reach the end of the array, store the current sum in our result list. This avoids explicitly storing subsets, reduces unnecessary operations, and still generates all sums in O(2^N) time. Sorting at the end gives the required increasing order.
def subset_sum(ind,sum,arr,ans):
    n=len(arr)
    if ind==n:
        ans.append(sum)
        return 
    subset_sum(ind+1,sum+arr[ind],arr,ans)
    subset_sum(ind+1,sum,arr,ans)
def find(arr,ans):
    subset_sum(0,0,arr,ans)
    ans.sort()
    return ans
arr=list(map(int,input("enter the array: ").split(',')))
ans=[]
print(find(arr,ans))



