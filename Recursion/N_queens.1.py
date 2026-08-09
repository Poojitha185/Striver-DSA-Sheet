#Time Complexity: O(N!), we try all possible permutations of placing the queens.
#Space Complexity: O(N), three boolean arrays are stored to check for safety.

def solve(col,board,ans,leftrow,upperdiagonal,lowerdiagonal,n):
    if col==n:
        ans.append([''.join(row) for row in board])
        return 
    for row in range(n):
     if(leftrow[row]==0 and upperdiagonal[(n-1)+(col-row)]==0 and lowerdiagonal[col+row]==0):
        board[row][col]="Q"
        leftrow[row]=1
        upperdiagonal[(n-1)+(col-row)]=1
        lowerdiagonal[col+row]=1
        solve(col+1,board,ans,leftrow,upperdiagonal,lowerdiagonal,n)
        board[row][col]="."
        leftrow[row]=0
        upperdiagonal[(n-1)+(col-row)]=0
        lowerdiagonal[col+row]=0
def Nqueens(n):
    board=[]
    for i in range(n):
      row=[]
      for j in range(n):
        row.append(".")
      board.append(row)
    ans=[]
    leftrow = [0] * n                      #it will create list with all indexes containing value as zero It won't cause an index error because the size 2*n - 1 is chosen specifically to cover all possible diagonal indices.
    upperdiagonal = [0] * (2 * n - 1)
    lowerdiagonal = [0] * (2 * n - 1)
    solve(0,board,ans,leftrow,upperdiagonal,lowerdiagonal,n)
    return ans
n=int(input("enter the value of n: "))
ans=Nqueens(n)
for i in ans:
   print(i)
