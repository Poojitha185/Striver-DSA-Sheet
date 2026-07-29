#Time Complexity: O(N × 2^N) More precisely, the recursion itself generates 2ⁿ subsets, but storing/converting each subset costs up to O(n).
#Space Complexity: O(N * 2^N). We store up to 2^N subsets in the set, each subset storing up to N elements in the worst case. Additionally, O(N) space is used for the recursion stack during subset generation.
def subset(ind,curr,arr,ans):
    n=len(arr)
    if ind==n:
        ans.add(tuple(curr))
        return 
    curr.append(arr[ind])
    subset(ind+1,curr,arr,ans)
    curr.pop()
    subset(ind+1,curr,arr,ans)
arr=list(map(int,input("enter the array: ").split(',')))
ans=set()
curr=[]
subset(0,curr,arr,ans)
print("the list of subsets are: ")
k=[]
for i in ans:
    k.append(list(i))
print(k)