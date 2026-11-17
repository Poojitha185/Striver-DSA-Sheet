#Time Complexity: O(N), where N is the size of the array. The helper function countAtMost runs in O(N), and it is called twice. So, the overall time complexity is O(2N), which simplifies to O(N).
#Space Complexity: O(N), because the frequency map may store distinct values from the current window

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