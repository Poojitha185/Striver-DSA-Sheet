#Time Complexity: O(n),We traverse the array twice: once to count, once to overwrite. Each operation is O(n).
#Space Complexity: O(1), We use only a constant number of counters regardless of the input size. No extra array is used.
def sort_0_1_2(arr,n):
    count1 = count2 = count3 = 0

    for num in arr:
     if num == 0:
        count1 += 1
     elif num == 1:
        count2 += 1
     else:
        count3 += 1
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