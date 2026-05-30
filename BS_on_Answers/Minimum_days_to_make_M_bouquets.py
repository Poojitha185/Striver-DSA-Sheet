class RoseGarden:
    # Function to check if it's possible to make 'm' bouquets on 'day'
    def is_possible(self, bloom_days, day, m, k):
        count = 0  # count of consecutive bloomed flowers
        bouquets = 0

        for bloom in bloom_days:
            if bloom <= day:
                count += 1
                if count == k:
                    bouquets += 1
                    count = 0
            else:
                count = 0

        return bouquets >= m

    # Main function to find the minimum day to make 'm' bouquets
    def min_days_to_make_bouquets(self, bloom_days, m, k):
        total_flowers = m * k
        if total_flowers > len(bloom_days):
            return -1

        low = min(bloom_days)
        high = max(bloom_days)

        for day in range(low, high + 1):
            if self.is_possible(bloom_days, day, m, k):
                return day

        return -1


# Example usage
bloom_days = [7, 7, 7, 7, 13, 11, 12, 7]
k = 3
m = 2

garden = RoseGarden()
result = garden.min_days_to_make_bouquets(bloom_days, m, k)

if result == -1:
    print("We cannot make m bouquets.")
else:
    print(f"We can make bouquets on day {result}")
