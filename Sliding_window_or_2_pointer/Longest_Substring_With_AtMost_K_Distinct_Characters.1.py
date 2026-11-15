#Time Complexity: O(N), where N represents the string length. Pointer right processes every character once, while pointer left moves only forward.
#Space Complexity: O(N), because the frequency map may contain up to N distinct characters for a general character set. A fixed-size character set reduces auxiliary space to O(1).

def longest_substring_at_most_k_distinct(s,k):
        max_length = 0
        l,r = 0,0
        frequency = {}
        while(r < len(s)):
                frequency[s[r]] = frequency.get(s[r], 0) + 1
                while len(frequency) > k:
                        frequency[s[l]] -= 1
                        if frequency[s[l]] == 0:
                                del frequency[s[l]]
                        l = l + 1
                max_length = max(max_length,r - l + 1)
                r = r + 1
        return max_length
s = input("Enter the string: ")
k = int(input("Enter the value of k: "))
print(longest_substring_at_most_k_distinct(s,k))