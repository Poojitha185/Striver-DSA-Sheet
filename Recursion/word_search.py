#Time Complexity: O(m * n * 4^L),We may start from each of the m×n cells, and explore up to 4 directions for each of the L letters in the word.
#Space Complexity: O(L),Recursion depth equals the length of the word; we also modify the board in-place, so no extra space for visited tracking.

#We can solve this using backtracking. Starting from each cell in the grid, we explore all four possible directions (up, down, left, right) to try to match the next character in the word. We mark visited cells temporarily to avoid reusing them, and backtrack when a path fails. This ensures we explore all possible connected sequences of characters in the board that might form the target word.
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
