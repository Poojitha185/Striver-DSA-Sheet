#Time Complexity: O(logN), in the algorithm, in every step, we are basically dividing the search space into 2 equal halves. This is actually equivalent to dividing the size of the array by 2, every time. After a certain number of divisions, the size will reduce to such an extent that we will not be able to divide that anymore and the process will stop. The number of total divisions will be equal to the time complexity. 
#Space Complexity: O(1), no extra space being used
#Binary Search approach(Recursive implementation)

def binary_search_recursive(arr,low,high,target,n):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif target>arr[mid]:
        return binary_search_recursive(arr,mid+1,high,target,n)
    else:
        return binary_search_recursive(arr,low,mid-1,target,n)
arr=list(map(int,input("enter the array: ").split(',')))
target=int(input("enter the target: "))
n=len(arr)
print("the target is found at index:",binary_search_recursive(arr,0,n-1,target,n))
