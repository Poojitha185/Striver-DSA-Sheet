#Time Complexity: O(N), We are traversing the whole array.

#Space Complexity: O(1), as we are not using any extra space.

#using linear search approach
def count_occurences(arr,n,target):
    count=0
    for i in range(n):
        if arr[i]==target:
            count+=1
    return count
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
target=int(input("enter the target: "))
print("the target is found",count_occurences(arr,n,target),"times in the array")