class MissingKFinder:
    # Binary search to find the k-th missing number
    def missing_k(self, vec, k):
        low, high = 0, len(vec) - 1

        while low <= high:
            mid = (low + high) // 2

            # Number of missing numbers before index mid
            missing = vec[mid] - (mid + 1)

            if missing < k:
                low = mid + 1  # Need more missing values, go right
            else:
                high = mid - 1  # Too many missing, go left

        # Final k-th missing number calculation
        return k + high + 1

# Driver code
vec = [4, 7, 9, 10]
k = 4

finder = MissingKFinder()
ans = finder.missing_k(vec, k)

print("The missing number is:", ans)
