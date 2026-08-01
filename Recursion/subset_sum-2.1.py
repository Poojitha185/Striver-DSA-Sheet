def subset(ind,curr,arr,ans):
    n=len(arr)
    ans.append(list(curr))
    for i in range(ind,n):
        if i>ind and arr[i]==arr[i-1]:    #i>ind is wrote bcz same elements containing combination can be skipped bcz of arr[i]==arr[i-1] condition this condition ensures that if same elements picking again at same position then only it can be that combionation to avoid duplicates.#
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
