import math

class Solution:
    # Function to calculate total hours at given speed
    def calculateTotalHours(self, piles, speed):
        totalH = 0
        for bananas in piles:
            totalH += math.ceil(bananas / speed)
        return totalH

    # Function to find minimum eating speed
    def minEatingSpeed(self, piles, h):
        # Find maximum element
        maxPile = max(piles)

        # Initialize low and high pointers
        low, high = 1, maxPile
        ans = maxPile

        # Binary search on answer space
        while low <= high:
            mid = (low + high) // 2
            totalH = self.calculateTotalHours(piles, mid)

            # If possible, try smaller speed
            if totalH <= h:
                ans = mid
                high = mid - 1
            # Otherwise, try larger speed
            else:
                low = mid + 1

        return ans

# Driver code
piles = [3, 6, 7, 11]
h = 8
obj = Solution()
print(obj.minEatingSpeed(piles, h))
