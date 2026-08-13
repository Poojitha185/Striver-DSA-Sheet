from typing import List

class Solution:
    # Check if placing character c at board[row][col] is valid
    def isValid(self, board: List[List[str]], row: int, col: int, c: str) -> bool:
        # Check each row for the same character in the current column
        for i in range(9):
            if board[i][col] == c:
                # Character already exists in this column - invalid placement
                return False
        
        # Check each column for the same character in the current row
        for j in range(9):
            if board[row][j] == c:
                # Character already exists in this row - invalid placement
                return False
        
        # Calculate the starting row index of the 3x3 sub-box
        boxRowStart = 3 * (row // 3)
        # Calculate the starting column index of the 3x3 sub-box
        boxColStart = 3 * (col // 3)
        
        # Check all cells in the 3x3 sub-box
        for i in range(3):
            for j in range(3):
                if board[boxRowStart + i][boxColStart + j] == c:
                    # Character found in the sub-box - invalid placement
                    return False
        
        # If no conflicts, placement is valid
        return True

    # Recursive backtracking function to solve the Sudoku board
    def solveSudoku(self, board: List[List[str]]) -> bool:
        # Iterate through all rows
        for i in range(9):
            # Iterate through all columns
            for j in range(9):
                # If current cell is empty (denoted by '.')
                if board[i][j] == '.':
                    # Try placing digits from '1' to '9' in this cell
                    for c in map(str, range(1, 10)):
                        # Check if placing c is valid
                        if self.isValid(board, i, j, c):
                            # Place c temporarily
                            board[i][j] = c
                            
                            # Recursively attempt to solve rest of the board
                            if self.solveSudoku(board):
                                return True
                            
                            # If placing c doesn't lead to a solution, backtrack
                            board[i][j] = '.'
                    
                    # If no digit fits here, trigger backtracking
                    return False
        # If all cells are filled correctly, return True to indicate success
        return True

# Driver code to test the solution
if __name__ == "__main__":
    board = [
        ['9', '5', '7', '.', '1', '3', '.', '8', '4'],
        ['4', '8', '3', '.', '5', '7', '1', '.', '6'],
        ['.', '1', '2', '.', '4', '9', '5', '3', '7'],
        ['1', '7', '.', '3', '.', '4', '9', '.', '2'],
        ['5', '.', '4', '9', '7', '.', '3', '6', '.'],
        ['3', '.', '9', '5', '.', '8', '7', '.', '1'],
        ['8', '4', '5', '7', '9', '.', '6', '1', '3'],
        ['.', '9', '1', '.', '3', '6', '.', '7', '5'],
        ['7', '.', '6', '1', '8', '5', '4', '.', '9']
    ]
    sol = Solution()
    # Solve the Sudoku board in-place
    sol.solveSudoku(board)
    # Print the solved Sudoku board row-wise
    for row in board:
        print(" ".join(row))
