#Time Complexity: O(N²), where N represents the string length. Expansion from every starting position may process many later characters.
#Space Complexity: O(N), because the frequency map may store many distinct characters for a general string.

def longest_substring_at_most_k_distinct(s,k):
        max_length = 0
        for start in range(len(s)):
            frequency = {}
            for end in range(start, len(s)):
                frequency[s[end]] = (frequency.get(s[end], 0) + 1)
                if len(frequency) > k:
                    break
                max_length = max(max_length,end - start + 1)
        return max_length

s=input("Enter the string: ")
k=int(input("Enter the value of k: "))
print(longest_substring_at_most_k_distinct(s,k))