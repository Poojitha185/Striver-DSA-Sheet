def reverse(s):
        # List to store words
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