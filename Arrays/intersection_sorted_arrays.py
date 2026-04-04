#TC:O(n1*n2), as we are using nested loops to compare each element of arr1 with each element of arr2.
#SC:O(n2), as we are using an additional visited array of size n2 to keep track of the elements in arr2 that have already been included in the intersection.
def intersection(arr1,arr2,n1,n2):
    visited=[0]*n2
    ans=[]
    for i in range(n1):
        for j in range(n2):
            if arr1[i]==arr2[j] and visited[j]==0:
                 ans.append(arr2[j])
                 visited[j]=1
                 break
            if arr2[j]>arr1[i]:
                break
    return ans
arr1=list(map(int,input("enter the first sorted arary: ").split(',')))
arr2=list(map(int,input("enter the second sorted arary: ").split(',')))
n1=len(arr1)
n2=len(arr2)
print("intersection of two sorted arrays: ",intersection(arr1,arr2,n1,n2))
