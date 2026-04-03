def union_sorted_arrays(arr1,arr2,n1,n2):
    i=0
    j=0
    union=[]
    while i<n1 and j<n2:
        if arr1[i]<arr2[j]:
            if len(union)==0 or union[-1]!=arr1[i]:
                union.append(arr1[i])
            i=i+1
        else:
            if len(union)==0 or union[-1]!=arr2[j]:
                union.append(arr2[j])
            j=j+1
    while(i<n1):
        if len(union)==0 or union[-1]!=arr1[i]:
                union.append(arr1[i])
        i=i+1
    while(j<n2):
         if len(union)==0 or union[-1]!=arr2[j]:
                union.append(arr2[j])
         j=j+1
    return union
arr1=list(map(int,input("enter the first sorted arary: ").split(',')))
arr2=list(map(int,input("enter the second sorted arary: ").split(',')))
n1=len(arr1)
n2=len(arr2)
print("union of two sorted arrays: ",union_sorted_arrays(arr1,arr2,n1,n2))