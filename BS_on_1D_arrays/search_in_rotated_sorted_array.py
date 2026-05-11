#Time Complexity: O(N),We may need to check every element in the worst case if the target is not present.

#Space Complexity: O(1),No extra space is used; only constant variables.

#linear search approach

def search(arr,n,target):
    for i in range(n):
        if arr[i]==target:
            return i
    return -1
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
target=int(input("enter the target: "))
print("the target is found at index:",search(arr,n,target))