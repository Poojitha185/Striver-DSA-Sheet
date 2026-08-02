#Time Complexity: O(2^N),In the worst case (all unique elements), we generate all possible subsets, which is 2^N. Sorting takes O(N log N), so total complexity is O(2^N + N log N) ≈ O(2^N).
#Space Complexity: O(N) ,Due to recursion depth and storage of the current subset in the call stack. The output storage is O(2^N) for all subsets.

#Instead of generating all subsets and then removing duplicates, we can avoid creating duplicates in the first place. This is done by sorting the input array first so that all duplicate numbers are adjacent. While generating subsets through backtracking, if we encounter a number that is the same as the previous one and it’s not the first in the current recursive call, we skip it. This pruning step ensures we only generate unique subsets without extra storage for duplicate removal.

#Sorting is essential here because without sorting, duplicates would be scattered and hard to skip correctly. This method is efficient and avoids unnecessary subset generation, making it better in both runtime and memory usage compared to the brute force approach.
#Sort the input array so that duplicates are adjacent.
#Initialize a list to store the current subset and a list of lists to store all unique subsets.Use a recursive backtracking function that: Adds the current subset to the list of results.Iterates from the current index to the end of the array.
#If the current element is the same as the previous one and not at the starting index of this recursion, skip it. Include the current element in the subset and recurse for the next index.
#Backtrack by removing the last added element.

def subset(ind,curr,arr,ans):
    n=len(arr)
    ans.append(list(curr))
    for i in range(ind,n):
        if i>ind and arr[i]==arr[i-1]:    #if we encounter a number that is the same as the previous one and it’s not the first in the current recursive call, we skip it.
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
