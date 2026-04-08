#Time Complexity: O(N²) because we use two nested loops to check every possible pair of elements in the array, where N is the size of the array.
#Space Complexity: O(1) as we use a constant amount of extra space regardless of input size.
def two_sum(arr,n,target):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                return "YES",[i,j]
                break
    return "NO",[-1,1]
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
target=int(input("enter the target sum: "))

status, indices = two_sum(arr, n, target)

print(status)
if status == "YES":
    print("The numbers present in indices:", indices)
else:    
    print("No such pair of numbers found in the array.")
