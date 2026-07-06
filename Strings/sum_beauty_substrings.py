# Function to compute beauty sum
#Time Complexity:

#Outer loop: O(n) (for each starting index)
#Inner loop: O(n) (for each ending index)
#Computing max and min for frequencies: O(26) in the worst case (since only lowercase letters), O(n^2 * 26) ≈ O(n^2) because 26 is constant.

#Space Complexity:
#Frequency map uses at most 26 characters → O(26) = O(1).
#No extra data structures apart from that.
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