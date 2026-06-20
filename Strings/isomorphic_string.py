#ord() converts a character into its ASCII (numeric) value.
def isomorphicString( s, t):
          # Arrays to track last seen positions of characters
          m1, m2 = [0] * 256, [0] * 256
          # Get the length of the strings
          n = len(s)
          # Loop through each character in both strings
          for i in range(n):
              # Return False if last seen positions don't match
              if m1[ord(s[i])] != m2[ord(t[i])]:
                  return False
              # Update last seen positions with current index + 1
              m1[ord(s[i])] = i + 1
              m2[ord(t[i])] = i + 1
          # Return True if no inconsistencies found
          return True
s=input("enter the first string: ")
t=input("enter the second string: ")
print("The two strings are isomorphic:",isomorphicString(s,t))