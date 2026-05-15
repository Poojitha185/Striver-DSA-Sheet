class Solution:
    def search_in_rotated_sorted_array_ii(self, arr, k):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            # If mid is the target
            if arr[mid] == k:
                return True

            # Cannot determine sorted half due to duplicates
            if arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1
                continue

            # Left half is sorted
            if arr[low] <= arr[mid]:
                if arr[low] <= k <= arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # Right half is sorted
                if arr[mid] <= k <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False


if __name__ == "__main__":
    arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
    k = 3
    sol = Solution()
    result = sol.search_in_rotated_sorted_array_ii(arr, k)

    if result:
        print("Target is present in the array.")
    else:
        print("Target is not present.")
