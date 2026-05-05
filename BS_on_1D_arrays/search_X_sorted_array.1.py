#Time Complexity: O(logN), in the algorithm, in every step, we are basically dividing the search space into 2 equal halves. This is actually equivalent to dividing the size of the array by 2, every time. After a certain number of divisions, the size will reduce to such an extent that we will not be able to divide that anymore and the process will stop. The number of total divisions will be equal to the time complexity. 
#Space Complexity: O(1), no extra space being used
#Binary Search approach(iterative implementation)

def binary_search(arr,target,n):
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif target>arr[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
target=int(input("enter the target: "))
print("the target is found at index:",binary_search(arr,target,n))