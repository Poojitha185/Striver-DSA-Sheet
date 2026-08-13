def solve(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==".":
                for k in range(1,10):
                    if(isvalid(board,i,j,str(k))):
                        board[i][j]=str(k)
                        if(solve(board)==True):
                           return True
                        else:
                           board[i][j]="."
                return False
    return True
def isvalid(board,row,col,c):
    for i in range(9):
        if(board[i][col]==c):
            return False
        if(board[row][i]==c):
            return False
        if(board[(3*(row//3))+(i//3)][(3*(col//3))+(i%3)]==c):
            return False
    return True
import ast
board = ast.literal_eval(input("Enter board: "))  
(solve(board))
for row in board:
    print(" ".join(row))