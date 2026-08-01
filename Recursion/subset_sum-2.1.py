#Time Complexity: O(2^N),In the worst case (all unique elements), we generate all possible subsets, which is 2^N. Sorting takes O(N log N), so total complexity is O(2^N + N log N) ≈ O(2^N).

#Space Complexity: O(N) ,Due to recursion depth and storage of the current subset in the call stack. The output storage is O(2^N) for all subsets.
def subset(ind,curr,arr,ans):
    n=len(arr)
    ans.append(list(curr))
    for i in range(ind,n):
        if i>ind and arr[i]==arr[i-1]:    #i>ind is wrote bcz same elements containing combination can be skipped bcz of arr[i]==arr[i-1] condition this condition ensures that if same elements picking again at same position then  that combionation is not taken to avoid duplicates.
                continue
        curr.append(arr[i])
        subset(i+1,curr,arr,ans)
        curr.pop()
def find(arr):
    arr.sort()
    ans=[]
    curr=[]
    subset(0,curr,arr,ans)
    return ans
arr=list(map(int,input("enter the array: ").split(',')))
arr.sort()
k=find(arr)
print("the list of subsets are: ")
print(k)
