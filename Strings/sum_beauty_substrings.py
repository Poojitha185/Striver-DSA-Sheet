# Function to compute beauty sum
def beauty_sum(s):
    n = len(s)
    total = 0

    # Loop over all substrings
    for i in range(n):
        freq = {}

        for j in range(i, n):
            # Increment frequency
            freq[s[j]] = freq.get(s[j], 0) + 1

            values = freq.values()
            maxi = max(values)
            mini = min(values)

            # Add difference
            total += (maxi - mini)

    return total

# Main function
def main():
    s = "xyx"
    print("Beauty Sum:", beauty_sum(s))

if __name__ == "__main__":
    main()