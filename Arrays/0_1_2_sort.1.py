def sort_0_1_2(arr,n):
    count1=arr.count(0)
    count2=arr.count(1)
    count3=arr.count(2)
    index=0
    for i in range(count1):
        arr[index]=0
        index +=1
    for i in range(count2):
        arr[index]=1
        index +=1
    for i in range(count3):
        arr[index]=2
        index+=1
    return arr
arr=list(map(int,input("enter the array: ").split(',')))
print("the array after sorting: ",sort_0_1_2(arr,len(arr)))