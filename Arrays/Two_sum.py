
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
