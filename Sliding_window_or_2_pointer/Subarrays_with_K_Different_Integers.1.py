#Time Complexity: O(N), where N is the size of the array. The helper function countAtMost runs in O(N), and it is called twice. So, the overall time complexity is O(2N), which simplifies to O(N).
#Space Complexity: O(N), because the frequency map may store distinct values from the current window

#A helper function countAtMost is created to count subarrays with at most limit distinct integers. If limit is less than or equal to 0, 0 is returned because no non-empty useful subarray can have at most 0 distinct integers.
#Inside the helper function, a frequency map is used to store how many times each integer appears in the current window. This is needed because an integer should be removed from the distinct count only when its frequency becomes 0.
#Two variables are initialized: left is set to 0 to represent the left boundary of the window, and count is set to 0 to store the number of valid subarrays.
#The right pointer moves from 0 to n - 1. At every step, nums[right] is added to the frequency map because it becomes part of the current window.
#If the size of the frequency map becomes greater than limit, the window is shrunk from the left. While shrinking, the frequency of nums[left] is decreased. If its frequency becomes 0, that integer is removed from the map. Then left is moved one step forward.
#Once the window contains at most limit distinct integers, every subarray ending at right and starting from any index between left and right is valid. Therefore, right - left + 1 is added to count. Finally, the answer is returned as countAtMost(k) - countAtMost(k - 1).

def at_most_k_distinct(arr, k):
        count = 0
        l = 0
        r = 0
        frequency = {}
        while r < len(arr):
                frequency[arr[r]] = frequency.get(arr[r], 0) + 1
                while len(frequency) > k:
                        frequency[arr[l]] -= 1
                        if frequency[arr[l]] == 0:
                                del frequency[arr[l]]
                        l = l + 1
                count = count + (r - l + 1)
                r = r + 1
        return count
def exactly_k_distinct(arr, k):
        return at_most_k_distinct(arr, k) - at_most_k_distinct(arr, k - 1)

arr = list(map(int, input("Enter the array: ").split(",")))
k = int(input("Enter the value of k: "))
print(exactly_k_distinct(arr, k))