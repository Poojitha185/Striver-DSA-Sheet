#Time Complexity: O(N³), where N represents the string length. O(N²) substrings exist, and every uniqueness check may scan up to N characters.if s[j] in l: takes O(N) in the worst case because l is a list.
#Space Complexity: O(N), because the helper list may store every character from one substring in the worst case.

def length_of_longest_substring(s):
        n = len(s)
        max_len = 0
        # Try every possible start.
        for i in range(n):
            l=[]
            # Extend the substring
            # from the current start.
            for j in range(i, n):
                if s[j] in l:           #if s[j] in l: takes O(N) in the worst case because l is a list.
                    break
                l.append(s[j])
                max_len = max(
                    max_len, j-i + 1)
        return max_len
s=input("enter the string: ")
print(length_of_longest_substring(s))