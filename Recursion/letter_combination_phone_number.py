#Time Complexity: O(4^N * N), where n is the length of the input digits. This is because each digit can map to up to 4 letters, and there are n digits.

#Space Complexity: O(N), where n is the length of the input digits. This is due to the recursion stack depth.
#For the digit at the current index, loop through all its mapped letters.
#For each letter, call the helper function again with the next index and the updated combination string.
def helper(digits, ans, index, current):
        k=["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        # Base case: if index reaches the end of digits
        if index == len(digits):
            # Add the current combination to the answer
            ans.append(current)
            return
        # Get characters corresponding to the current digit
        s = k[int(digits[index])]
        # Loop through the corresponding characters
        for char in s:
            # Recursively call function with next index
            # Add current character to the string
            helper(digits, ans, index + 1, current + char)

    # Function to get all letter combinations for a given digit string
def letterCombinations(digits):
        ans = []  # List to store results
        # Return empty list if digits string is empty
        if not digits:
            return ans
        # Initiate recursive function
        helper(digits, ans, 0, "")
        return ans  # Return the result
digits=input("enter the digits: ")
result=letterCombinations(digits)
print(result)