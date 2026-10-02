def length_of_longest_substring(s):
        n = len(s)
        max_len = 0
        # Try every possible start.
        for i in range(n):
            l=[]
            # Extend the substring
            # from the current start.
            for j in range(i, n):
                if s[j] in l:
                    break
                l.append(s[j])
                max_len = max(
                    max_len, j-i + 1)
        return max_len
s=input("enter the string: ")
print(length_of_longest_substring(s))