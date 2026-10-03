#Time Complexity: O(N²), where N represents the string length. Expansion from each starting position may scan many later characters.
#Space Complexity: O(N), because the set may store every distinct character from one growing substring.

def length_of_longest_substring(s):
        n = len(s)
        max_len = 0
        # Try every possible start.
        for i in range(n):
            l=set()                     # Use a set to store characters for O(1) lookups
            # Extend the substring
            # from the current start.
            for j in range(i, n):
                if s[j] in l:           # if s[j] in l: takes O(1), because l is a set.
                    break
                l.add(s[j])
                max_len = max(max_len, j-i + 1)
        return max_len
s=input("enter the string: ")
print(length_of_longest_substring(s))