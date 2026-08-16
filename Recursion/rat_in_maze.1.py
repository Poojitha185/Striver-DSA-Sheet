#Time Complexity: O(4^(N*N)),, because on every cell we need to try 4 different directions.

#Space Complexity: O(N*N), additional space for visited array and maximum Depth of the recursion tree(auxiliary space).

#when they give directions more than 4 for example 8 then we have to use more if conditions like one condition for each direction thats why we created two di and dj arrays with direction values and using one single for loop we can handle all 4 directions here 

def solve(i,j,n,maze,visited,ans,move,di,dj):
    if(i==n-1 and j==n-1):                        #base case
        ans.append(move)
        return
    direction='DLRU'
    for ind in range(4):
        nexti=i+di[ind]
        nextj=j+dj[ind]
        if(nexti>=0 and nextj>=0 and nexti<n and nextj<n and not visited[nexti][nextj] and maze[nexti][nextj]==1 ):
            visited[i][j]=1
            solve(nexti,nextj,n,maze,visited,ans,move+direction[ind],di,dj)
            visited[i][j]=0

import ast
maze = ast.literal_eval(input("Enter the maze: "))      #is used because when you type a 2D list through input(), Python initially receives it as a string.   ast.literal_eval(...) takes that string and converts it into the corresponding Python data structure.
n=len(maze)
visited = [[0 for _ in range(n)] for _ in range(n)]
ans=[]
di=[1,0,0,-1]
dj=[0,-1,1,0]
if maze[0][0]==1:
   solve(0,0,n,maze,visited,ans,"",di,dj)
print(ans)