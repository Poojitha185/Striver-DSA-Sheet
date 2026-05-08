#Time Complexity: O(logN), where N = size of the given array.

#Space Complexity: O(1) as we are using no extra space.
def search_insert(arr, x, n):
        low, high = 0, n - 1
        ans = n  

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= x:
                ans = mid  # Potential answer, look on left side
                high = mid - 1
            else:
                low = mid + 1  # Look on right side

        return ans
arr=list(map(int,input("enter the array: ").split(',')))
target=int(input("enter the target: "))
n=len(arr)
print("the target is found at index:",search_insert(arr,target,n))

