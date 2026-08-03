#Time Complexity: O(4^N * N), where n is the length of the input digits. This is because each digit can map to up to 4 letters, and there are n digits.

#Space Complexity: O(N), where n is the length of the input digits. This is due to the recursion stack depth.
class Solution:
    def __init__(self):
        # Mapping digits to corresponding characters
        self.map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    # Recursive helper function to generate combinations
    def helper(self, digits, ans, index, current):
        # Base case: if index reaches the end of digits
        if index == len(digits):
            # Add the current combination to the answer
            ans.append(current)
            return
        # Get characters corresponding to the current digit
        s = self.map[int(digits[index])]
        # Loop through the corresponding characters
        for char in s:
            # Recursively call function with next index
            # Add current character to the string
            self.helper(digits, ans, index + 1, current + char)

    # Function to get all letter combinations for a given digit string
    def letterCombinations(self, digits):
        ans = []  # List to store results
        # Return empty list if digits string is empty
        if not digits:
            return ans
        # Initiate recursive function
        self.helper(digits, ans, 0, "")
        return ans  # Return the result
if __name__ == "__main__":
    solution = Solution()
    digits = "23"  # Input digits
    result = solution.letterCombinations(digits)  # Get combinations

    # Print the results
    print(result)