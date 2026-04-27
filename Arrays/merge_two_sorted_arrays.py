def merge_two_sorted_arrays(arr1,arr2):
    i=0
    j=0
    while(i<len(arr1)):
        while(j<len(arr2)):
         if arr1[i]>arr2[j]:
              arr1[i]=arr2[j]
              j=j+1
         i=i+1
         j=j+1
    if len(arr1)<len(arr2):
        while(j<len(arr2)):
            arr1[i]=arr2[j]
            j=j+1
    return arr1
arr1=list(map(int,input("enter the first array: ").split(',')))
arr2=list(map(int,input("enter the second array: ").split(',')))
print("merged array: ",merge_two_sorted_arrays(arr1,arr2))
