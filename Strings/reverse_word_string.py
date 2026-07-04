class Solution:
    # Function to reverse the order of words in a string
    def reverseWords(self, s: str) -> str:
        # List to store words
        words = []
        
        # Temporary variable to store current word
        word = ""
        
        # Traverse each character in the string
        for ch in s:
            # If not space, add character to word
            if ch != " ":
                word += ch
            # If space and we have collected a word
            elif word:
                # Add word to list
                words.append(word)
                # Reset word
                word = ""
        
        # Add the last word if present
        if word:
            words.append(word)
        
        # Reverse the list of words
        words.reverse()
        
        # Join with single space
        return " ".join(words)

# Driver code
if __name__ == "__main__":
    obj = Solution()
    s = " amazing coding skills "
    print(obj.reverseWords(s))
