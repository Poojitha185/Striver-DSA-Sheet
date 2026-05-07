#Time Complexity: O(logN), where N = size of the given array.

#Space Complexity: O(1) as we are using no extra space.

class BinarySearchInsert:
    def search_insert(self, arr, x):
        n = len(arr)
        low, high = 0, n - 1
        ans = n  # Default if x is larger than all elements

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= x:
                ans = mid  # Potential answer, look on left side
                high = mid - 1
            else:
                low = mid + 1  # Look on right side

        return ans

# Main execution
if __name__ == "__main__":
    arr = [1, 2, 4, 7]
    x = 6
    obj = BinarySearchInsert()
    index = obj.search_insert(arr, x)
    print(f"The index is: {index}")
