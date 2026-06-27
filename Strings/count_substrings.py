#Time Complexity: O(n) for each call to atMostKDistinct.

#Space Complexity: O(1) map size bounded by 26 characters for alphabets.

#Use a sliding window with two pointers (left and right) and a frequency map. Expand the window by moving the right pointer and count characters. If the count of distinct characters exceeds k, shrink the window by moving the left pointer. For each valid window, add (right - left + 1) to the result.

def at_most_k_distinct(s, k):
    left, res = 0, 0
    freq = {}

    # Iterate with right pointer
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        # Shrink window if distinct characters exceed k
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        # Count substrings in current window
        res += (right - left + 1)
    return res

# Function to count substrings with exactly k distinct characters
def count_substrings(s, k):
    return at_most_k_distinct(s, k) - at_most_k_distinct(s, k - 1)

def main():
    # Sample test
    s = "pqpqs"
    k = 2

    # Output the result
    print("Count:", count_substrings(s, k))  # Output: 7

if __name__ == "__main__":
    main()