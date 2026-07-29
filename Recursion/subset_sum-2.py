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