#Time Complexity: O(N * log N + M), where N is the number of strings and M is the minimum length of a string. The sorting operation takes O(N * log N) time, and the comparison of characters in the first and last strings takes O(M) time.

#Space Complexity: O(M), as the ans variable can store the length of the prefix which in the worst case will be O(M).

#The common prefix across all strings must exist between the smallest and largest string when sorted lexicographically.
#The point at which the characters start differing marks the end of the shared prefix.
# The portion before this mismatch is the longest common prefix among all strings.

def largest_common_prefix(strs,n):
    strs.sort()  # Sort the list of strings to bring similar prefixes together
    first=strs[0]
    last=strs[-1]
    ans=[]
    for i in range(min(len(first),len(last))):
        if first[i]!=last[i]:
            return ''.join(ans)
        ans.append(first[i])                   # or first[i] == last[i]
    return ''.join(ans)
strs = eval(input("Enter list of strings: "))  #whenever you want to type the input exactly as a Python list, matrix, tuple, or dictionary, eval() can convert it directly into the corresponding Python object.
n=len(strs)
print("The longest common prefix is:", largest_common_prefix(strs,n))
