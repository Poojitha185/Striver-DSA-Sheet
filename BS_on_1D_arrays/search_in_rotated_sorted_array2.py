#Time Complexity: O(N), N = size of the given array.

#Space Complexity: O(1), no extra space used.

#using linear search approach

def search(arr,n,target):
    for i in range(n):
        if arr[i]==target:
            return True
    return False
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
target=int(input("enter the target: "))
print(search(arr,n,target))