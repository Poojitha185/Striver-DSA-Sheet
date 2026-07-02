# Function to count substrings with at most k distinct characters
#Time Complexity: O(n) for each call to atMostKDistinct.
#Space Complexity: O(1) map size bounded by 26 characters for alphabets.
#Define a helper function atMostKDistinct(s, k) Use a sliding window with two pointers (left and right) and a frequency map. Expand the window by moving the right pointer and count characters. If the count of distinct characters exceeds k, shrink the window by moving the left pointer.

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

#For each valid window, add (right - left + 1) to the result.
#To find substrings with exactly k distinct characters, calculate: atMostKDistinct(s, k) - atMostKDistinct(s, k-1)
def count_substrings(s, k):
    return at_most_k_distinct(s, k) - at_most_k_distinct(s, k - 1)
s=input("Enter the string: ")
k=int(input("Enter the value of k: "))
result = count_substrings(s, k)
print("Number of substrings with exactly", k, "distinct characters:", result)