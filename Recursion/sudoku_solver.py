#Time Complexity: O(9(n ^ 2)), in the worst case, for each cell in the n2 board, we have 9 possible numbers.

#Space Complexity: O(1), since we are refilling the given board itself, there is no extra space required, so constant space complexity.

#Since we have to fill the empty cells with available possible numbers and we can also have multiple solutions, the main intuition is to try every possible way of filling the empty cells. And the more correct way to try all possible solutions is to use recursion. In each call to the recursive function, we just try all the possible numbers for a particular cell and transfer the updated board to the next recursive call.

def solve(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==".":
                for k in range(1,10):
                    if(isvalid(board,i,j,str(k))):          #bcz list contain elements as strings
                        board[i][j]=str(k)
                        if(solve(board)==True):
                           return True
                        else:
                           board[i][j]="."
                return False
    return True

#Validating Board
#Now, let's see how we are validating the sudoku board. After determining a number for a cell(at i'th row, j'th col), we try to check the validity. As we know, a valid sudoku needs to satisfy 3 conditions, we can use three loops. But we can do within a single loop itself. Let's try to understand that.
#We loop from 0 to 8 and check the values - board[i][col](1st condition) and board[row][i](2nd condition), whether the number is already included. For the 3rd condition - the expression (3 * (row / 3) + i / 3) evaluates to the row numbers of that 3x3 submatrix and the expression (3 * (col / 3) + i % 3) evaluates to the column numbers.
#For eg, if row= 5 and col= 3, the cells visited are It covers all the cells in the sub-matrix.

def isvalid(board,row,col,c):
    for i in range(9):
        if(board[i][col]==c):
            return False
        if(board[row][i]==c):
            return False
        if(board[(3*(row//3))+(i//3)][(3*(col//3))+(i%3)]==c):     # we used 3 bcz each box in 9*9 contain 3 elements 
                                                                   #(i//3) to get quotient bcz quotient remains same till 3 elements 
            return False                                           #(i%3) to get remainderit changes every single time it is taken bcz column for ever single element it changes every single time
    return True

import ast                                                          # #You can convert the entered string into a Python list using ast.literal_eval()
board = ast.literal_eval(input("Enter board: "))  
(solve(board))
for row in board:
    print(" ".join(row))