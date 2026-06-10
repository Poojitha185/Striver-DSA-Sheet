#TC:Merging arrays: O(m + n)
#SC:Extra space for merged array: O(m + n)

def median(arr1,arr2,m,n):
    i=0
    j=0
    k=[]
    while(i<m and j<n):
        if arr1[i]<arr2[j]:
            k.append(arr1[i])
            i=i+1
        else:
            k.append(arr2[j])
            j=j+1
    while(i<m):
        k.append(arr1[i])
        i=i+1
    while(j<n):
        k.append(arr2[j])
        j=j+1
    if (len(k))%2==0:
        return(k[len(k)//2 - 1] + k[len(k)//2]) / 2
    else:
        return k[len(k)//2]
arr1=list(map(int,input("enter the first array: ").split(',')))
arr2=list(map(int,input("enter the first array: ").split(',')))
m=len(arr1)
n=len(arr2)
print("The median of 2 sorted arrays: ",median(arr1,arr2,m,n))
