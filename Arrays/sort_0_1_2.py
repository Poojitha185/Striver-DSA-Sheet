def sort_0_1_2(arr):
    arr.sort()
    return arr
arr=list(map(int,input("enter the array: ").split(',')))
print("the array after sorting: ",sort_0_1_2(arr))