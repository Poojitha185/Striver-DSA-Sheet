# Function to count substrings with at most k distinct characters
#Time Complexity: O(n) for each call to atMostKDistinct.

#Space Complexity: O(1) map size bounded by 26 characters for alphabets.

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
s=input("Enter the string: ")
k=int(input("Enter the value of k: "))
result = count_substrings(s, k)
print("Number of substrings with exactly", k, "distinct characters:", result)