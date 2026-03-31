def remove_duplicates(arr,n):
    set_1=set()
    index=0
    for i in arr:
        if i not in set_1:      #this condition is needed ,eventhough set_1 sores unique elemnents but duplicate element may be added arr[index]=i with this step set doenot control this
         set_1.add(i)
         arr[index]=i
         index=index+1
    return index
arr=arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
k=remove_duplicates(arr,n)
print("The number of unique elements are: ",k)
print("array after removing elements are:", arr[:k])    #algorithm updates only first k elements which are unique

