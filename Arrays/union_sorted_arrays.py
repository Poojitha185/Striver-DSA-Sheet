def union_sorted_arrays(arr1,arr2):
    k=set(arr1)|set(arr2)
    return sorted(k)
arr1=list(map(int,input("enter the first sorted arary: ").split(',')))
arr2=list(map(int,input("enter the second sorted arary: ").split(',')))
print("union of two sorted arrays: ",union_sorted_arrays(arr1,arr2))