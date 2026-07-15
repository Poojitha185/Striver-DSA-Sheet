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

    # Recurse
    return helper(s, i + 1, num, sign)

def myAtoi(s):
    i = 0

    # Skip whitespaces
    while i < len(s) and s[i] == ' ':
        i += 1

    # Handle sign
    sign = 1
    if i < len(s) and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1

    # Recursive helper
    return helper(s, i, 0, sign)

if __name__ == "__main__":
    s = "  -12345"
    print(myAtoi(s))  # Output: -12345