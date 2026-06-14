#Time Complexity: O(N+M), where N = given row number, M = given column number. We are starting traversal from (0, M-1), and at most, we can end up being in the cell (M-1, 0). So, the total distance can be at most (N+M). So, the time complexity is O(N+M).

#Space Complexity: O(1) as we are not using any extra space.

from typing import List

# Class to perform staircase search in a 2D row and column-wise sorted matrix
class MatrixSearch:
    def __init__(self, matrix: List[List[int]]):
        """
        Initialize the matrix search object.
        :param matrix: 2D list representing the sorted matrix
        """
        self.matrix = matrix

    def search_element(self, target: int) -> bool:
        """
        Search for the target element using staircase search.
        Start from the top-right corner and move left or down depending on value.
        Time complexity: O(n + m)
        :param target: Integer to search for
        :return: True if target exists in matrix, False otherwise
        """
        n = len(self.matrix)       # Number of rows
        m = len(self.matrix[0])    # Number of columns

        row = 0            # Start at first row
        col = m - 1        # Start at last column (top-right)

        # Loop until we go out of matrix bounds
        while row < n and col >= 0:
            current = self.matrix[row][col]  # Current element
            if current == target:
                return True  # Found target
            elif current < target:
                row += 1     # Move down to next row
            else:
                col -= 1     # Move left to previous column

        # Target not found after traversing
        return False


if __name__ == "__main__":
    # Example matrix
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    ms = MatrixSearch(matrix)
    found = ms.search_element(8)
    print(found)  # True
