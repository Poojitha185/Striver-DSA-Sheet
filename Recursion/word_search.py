
def search_by_dfs(i,j,idx,board,word,rows,cols):
  if idx==len(word):
    return True
  if i<0 or j<0 or i>=rows or j>=cols or board[i][j]!=word[idx]:
    return False
  temp=board[i][j]
  board[i][j]='#'           #backtracking
  found=(search_by_dfs(i+1,j,idx+1,board,word,rows,cols) or search_by_dfs(i-1,j,idx+1,board,word,rows,cols) or search_by_dfs(i,j+1,idx+1,board,word,rows,cols) or search_by_dfs(i,j-1,idx+1,board,word,rows,cols))
  board[i][j]=temp
  return found
def exist(rows,cols,board,word):
  for i in range(rows):
    for j in range(cols):
      if search_by_dfs(i,j,0,board,word,rows,cols):
        return True
  return False                                     #return False outside the loops allows the loops to continue when DFS fails. return True inside the loop immediately stops everything when the word is found.
import ast
board = ast.literal_eval(input("Enter board: "))   #You can convert the entered string into a Python list using ast.literal_eval()
rows=len(board)
cols=len(board[0])
word=input("enter the word to search: ")
print(exist(rows,cols,board,word))
