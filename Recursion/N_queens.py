class Solution:
    # Function to check if placing a queen is safe
    def isSafe(self, row, col, board, n):
        # Check left in same row
        for j in range(col):
            if board[row][j] == 'Q':
                return False

        # Check upper-left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check lower-left diagonal
        i, j = row, col
        while i < n and j >= 0:
            if board[i][j] == 'Q':
                return False
            i += 1
            j -= 1

        # Return true if safe
        return True

    # Backtracking function
    def solve(self, col, board, ans, n):
        # If all columns are filled
        if col == n:
            temp = [''.join(row) for row in board]
            ans.append(temp)
            return

        # Try placing in each row
        for row in range(n):
            if self.isSafe(row, col, board, n):
                # Place queen
                board[row][col] = 'Q'       
                # Recurse
                self.solve(col + 1, board, ans, n)  
                # Backtrack
                board[row][col] = '.'       
    # Main function
    def solveNQueens(self, n):
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        self.solve(0, board, ans, n)
        return ans
# Driver code
if __name__ == "__main__":
    # Create object
    obj = Solution()
    # Set size
    n = 4
    # Solve
    res = obj.solveNQueens(n)

    # Print solutions
    for board in res:
        for row in board:
            print(row)
        print()
