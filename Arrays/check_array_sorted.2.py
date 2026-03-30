#Time Complexity: O(N), as it checks each adjacent pair once in a single pass through the array.
#Space Complexity: O(1), as it uses constant extra space regardless of input size.
#optimal approach(compare adjacent elements)
def is_sorted(arr,n):
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False
    return True
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print(is_sorted(arr,n))        