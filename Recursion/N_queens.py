def issafe(row,col,n,board):
    r=row
    c=col
    while(r>=0 and c>=0):
        if board[r][c]=="Q":
            return False
        r-=1
        c-=1
    r=row
    c=col
    while(c>=0):
        if board[r][c]=='Q':
            return False
        c-=1
    r=row
    c=col
    while(r<n and c>=0):
        if board[r][c]=="Q":
            return False
        r+=1
        c-=1
    return True
def solve(col,board,ans,n):
    if col == n:
        ans.append([row[:] for row in board])
        return
    for i in range(n):
        if(issafe(i,col,n,board)):
            board[i][col]="Q"
            solve(col+1,board,ans,n)
            board[i][col]="."
def Nqueens(n):
    board = []
    for i in range(n):
       row = []
       for j in range(n):
           row.append(".")
       board.append(row)
    ans=[]
    solve(0,board,ans,n)
    return ans
n=int(input("enter the value of n: "))
ans=Nqueens(n)
for i in ans:
    for j in i:
        print(j)

