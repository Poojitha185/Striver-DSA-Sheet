#Time Complexity: O(n) since each character is processed once.

#Space Complexity: O(n) since the recursion stack grows up to n calls.

#Define a helper function that takes the string s, current index i, current result num, and sign.
#Recursively skip leading whitespaces until a non-whitespace character is found.
#Handle the sign if present (positive or negative).
#Recursively process each digit:

INT_MIN = -2**31
INT_MAX = 2**31 - 1

def helper(s, i, num, sign):
    # Base case: end of string or non-digit
    if i >= len(s) or not s[i].isdigit():
        return sign * num
    # Update num
    num = num * 10 + int(s[i])
    # Clamp if overflow
    if sign * num <= INT_MIN: return INT_MIN
    if sign * num >= INT_MAX: return INT_MAX
    return helper(s, i + 1, num, sign)
def myAtoi(s):
    i = 0
    while i < len(s) and s[i] == ' ':
        i += 1
    sign = 1
    if i < len(s) and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1
    return helper(s, i, 0, sign)
s=input("Enter a string: ")
result = myAtoi(s)
print("The integer value is:", result)