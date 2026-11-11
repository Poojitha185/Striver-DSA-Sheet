#Time Complexity: O(N²), where N represents the string length. Expansion from every starting position may process many later characters.
#Space Complexity: O(N), because the frequency map may store many distinct characters for a general string.

#Initialize maxLength with 0 for storing the best valid length found so far.
#Select every start index and create a fresh frequency map, because each starting position begins an independent expansion.
#Move end from start toward n - 1 and increase the frequency of s[end] after adding the current character.
#Stop expansion when the map size exceeds k, because every longer substring from the same start will retain more than k distinct characters.
#Update maxLength with end - start + 1 for every valid expansion, then return maxLength after processing all starting positions.

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