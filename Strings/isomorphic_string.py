#Time Complexity: O(N) where N is the length of the input strings, due to the single loop iterating through each character.
#Space Complexity: O(1) since the space used by the arrays is constant (256 fixed size) regardless of input size
#Use two fixed-size arrays (size 256) to track the last-seen positions of characters from each string.
#While scanning both strings together, compare if the characters at the current position have been seen at the same relative positions before.
#If not, it indicates inconsistent mapping — one character maps to multiple others — return false.
#If consistent, update the last seen position of both characters to ensure future checks remain valid.
def isomorphicString( s, t):
          # Arrays to track last seen positions of characters
          m1, m2 = [0] * 256, [0] * 256
          # Get the length of the strings
          n = len(s)                                     # Loop through each character in both strings
          for i in range(n):                             # Return False if last seen positions don't match
              if m1[ord(s[i])] != m2[ord(t[i])]:         #ord() converts a character into its ASCII (numeric) value.
                  return False
              # Update last seen positions with current index + 1
              m1[ord(s[i])] = i + 1
              m2[ord(t[i])] = i + 1
          # Return True if no inconsistencies found
          return True
s=input("enter the first string: ")
t=input("enter the second string: ")
print("The two strings are isomorphic:",isomorphicString(s,t))