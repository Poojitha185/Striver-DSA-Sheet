#Time Complexity: O(N),We traverse the string once to collect words (O(N)) and once more to reverse and join them (O(N)). Hence total time is O(N).

#Space Complexity: O(N),We store all words in a separate list/array, requiring extra space proportional to the number of characters.

def reverse(s):
        words = []
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
                word = ""                         # Reset word for next iteration
        if word:                                  #is necessary to capture the final word when the string does not end with a space.
            words.append(word)
        words.reverse()
        return " ".join(words)
s=input("enter string:")
print("reversing of string: ",reverse(s))