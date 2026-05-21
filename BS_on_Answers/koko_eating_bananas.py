import math

class Solution:
    # Function to calculate total hours for given speed
    def calculateTotalHours(self, a, hourly):
        totalHours = 0
        for pile in a:
            # Add hours using ceil
            totalHours += math.ceil(pile / hourly)
        return totalHours

    # Function to find minimum eating speed
    def minEatingSpeed(self, a, h):
        # Find maximum pile size
        maxVal = max(a)

        # Try every possible speed
        for i in range(1, maxVal + 1):
            hours = self.calculateTotalHours(a, i)

            # If hours fit within h
            if hours <= h:
                return i
        return maxVal

# Driver code
a = [3, 6, 7, 11]
h = 8
obj = Solution()
print(obj.minEatingSpeed(a, h))