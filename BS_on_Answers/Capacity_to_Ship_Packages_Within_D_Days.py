class Solution:
    # Function to check how many days needed for given capacity
    def daysNeeded(self, weights, capacity):
        # Initialize day count to 1
        days = 1
        # Current load for the day
        currentLoad = 0

        # Iterate over all package weights
        for w in weights:
            # If adding weight exceeds capacity
            if currentLoad + w > capacity:
                # Increase day count and reset load
                days += 1
                currentLoad = w
            else:
                # Otherwise, add weight to current load
                currentLoad += w
        # Return total days needed
        return days

    # Function to find minimum ship capacity to ship in d days
    def shipWithinDays(self, weights, d):
        # Find maximum weight as minimum capacity
        left = max(weights)
        # Find total sum as maximum capacity
        right = sum(weights)

        # Iterate from minimum to maximum capacity
        for capacity in range(left, right + 1):
            # Calculate days needed for current capacity
            needed = self.daysNeeded(weights, capacity)
            # If days needed are less than or equal to d, return capacity
            if needed <= d:
                return capacity
        # Should never reach here given constraints
        return right


if __name__ == "__main__":
    # Input weights
    weights = [5,4,5,2,3,4,5,6]
    # Days to ship
    d = 5
    # Create Solution instance
    sol = Solution()
    # Call the function and print result
    print(sol.shipWithinDays(weights, d))
