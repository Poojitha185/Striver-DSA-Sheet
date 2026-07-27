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



