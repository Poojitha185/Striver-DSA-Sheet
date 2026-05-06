#Time Complexity: O(N), where N = size of the given array.
#Space Complexity: O(1), no extra space used.
#using linear search
def upper_bound(arr,n,x):
    for i in range(n):
        if arr[i]>x:
            return i
    return n
arr=list(map(int,input("enter the array: ").split(',')))
x=int(input("enter the target: "))
n=len(arr)
print("the target is found at index:",upper_bound(arr,n,x))