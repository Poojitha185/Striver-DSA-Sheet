#Time Complexity: O(logN) for the best and average case. O(N/2) for the worst case. Here, N = size of the given array.

#Space Complexity: O(1), no extra space used

#same code as search_in_rotated_sorted_array.1.py but with a modification to handle duplicates in the array. If the low, mid, and high elements are equal, we cannot determine which half is sorted, so we move both pointers inward to skip the duplicates.

def search(arr,n,target):
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return True
        if arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1
                continue
        if arr[low]<=arr[mid]:
            if arr[low]<=target<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<target<=arr[high]:
                low=high+1
            else:
                high=mid-1
    return False
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
target=int(input("enter the target: "))
print(search(arr,n,target))