class RoseGarden:

    # Function to check if we can form m bouquets by 'day'
    def is_possible(self, bloom_days, day, m, k):
        count = 0  # count of consecutive bloomed flowers
        bouquets = 0  # number of bouquets formed

        for bloom in bloom_days:
            if bloom <= day:
                count += 1
                if count == k:
                    bouquets += 1  # one bouquet formed
                    count = 0
            else:
                count = 0  # reset if a flower is not ready

        return bouquets >= m

    # Main function to find the minimum day to make m bouquets
    def rose_garden(self, bloom_days, k, m):
        if m * k > len(bloom_days):
            return -1  # not enough flowers

        low = min(bloom_days)
        high = max(bloom_days)
        answer = -1

        while low <= high:
            mid = (low + high) // 2
            if self.is_possible(bloom_days, mid, m, k):
                answer = mid  # try to find smaller day
                high = mid - 1
            else:
                low = mid + 1  # need more days

        return answer


# Driver code
garden = RoseGarden()
bloom_days = [7, 7, 7, 7, 13, 11, 12, 7]
k = 3
m = 2
result = garden.rose_garden(bloom_days, k, m)
if result == -1:
    print("We cannot make m bouquets.")
else:
    print(f"We can make bouquets on day {result}")
