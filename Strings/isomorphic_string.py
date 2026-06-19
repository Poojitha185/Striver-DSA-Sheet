#Time Complexity: O(N) where N is the length of the input strings, due to the single loop iterating through each character.

#Space Complexity: O(1) since the space used by the arrays is constant (256 fixed size) regardless of input size
class Solution:
      # Method to check if two strings are isomorphic
      def isomorphicString(self, s, t):
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
  
  # Driver code to test the method
if __name__ == "__main__":
      # Create an instance of Solution
      solution = Solution()
  
      # Input strings
      s = "paper"
      t = "title"
  
      # Check and print whether strings are isomorphic
      if solution.isomorphicString(s, t):
          print("Strings are isomorphic.")
      else:
          print("Strings are not isomorphic.")