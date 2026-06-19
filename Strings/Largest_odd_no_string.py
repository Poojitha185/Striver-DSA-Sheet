#Time Complexity: O(N), since the loop runs once through the string of length N.

#Space Complexity: O(1), as we are using only a constant amount of extra space.
#An odd number must end with an odd digit, so we look for the last odd digit when scanning from the end.
#Leading zeroes don’t add value to the number, so we aim to remove them for a cleaner representation.
#Once the endpoint (last odd digit) is determined, we identify the starting point by skipping any leading zeroes before it.
#Extract the portion between these two positions, this gives the largest possible odd integer from the string.

def largest_odd_string(s,n):
    ind=0
    for i in range(n-1,-1,-1):
        if (int(s[i])%2)==1:
            ind=i
            break
    i=0
    while i<=ind and s[i]=='0':
        i=i+1
    return s[i:ind+1]
s=input("Enter the string: ")
n=len(s)
print("The largest odd number in the string is:",largest_odd_string(s,n))