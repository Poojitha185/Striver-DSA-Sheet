#Time Complexity: O(4^(N*N)),, because on every cell we need to try 4 different directions.

#Space Complexity: O(N*N), additional space for visited array and maximum Depth of the recursion tree(auxiliary space).

#Since the rat need to find all the paths to reach destination it should explore the maze step by step, trying every possible direction at each junction. If it reaches a dead end or an already visited cell, it backs up to the last decision point and tries another route. This way, it explores all possible paths from the start to the destination without missing any options. By marking cells as visited when moving forward and unmarking them when stepping back, the rat avoids infinite loops and ensures every path is explored exactly once.

def solve(i,j,n,maze,visited,ans,move):
    if(i==n-1 and j==n-1):                        #base case
        ans.append(move)
        return
    #downward                                     #D,L,R,U -> lexograpical order gives answer array with all path are in lexographical order
    if(i+1<n and not visited[i][j] and maze[i+1][j]==1 ):
      visited[i][j]=1
      solve(i+1,j,n,maze,visited,ans,move+"D")
      visited[i][j]=0
    #left
    if(j-1>=0 and not visited[i][j] and maze[i][j-1]==1 ):
          visited[i][j]=1
          solve(i,j-1,n,maze,visited,ans,move+"L")
          visited[i][j]=0
    #Right
    if(j+1<n and not visited[i][j] and maze[i][j+1]==1 ):
          visited[i][j]=1
          solve(i,j+1,n,maze,visited,ans,move+"R")
          visited[i][j]=0       #backtarcking
    #upwards
    if(i-1>=0 and not visited[i][j] and maze[i-1][j]==1 ):
          visited[i][j]=1
          solve(i-1,j,n,maze,visited,ans,move+"U")
          visited[i][j]=0

import ast
maze = ast.literal_eval(input("Enter the maze: "))      #is used because when you type a 2D list through input(), Python initially receives it as a string.   ast.literal_eval(...) takes that string and converts it into the corresponding Python data structure.
n=len(maze)
visited = [[0 for _ in range(n)] for _ in range(n)]
ans=[]
if maze[0][0]==1:
   solve(0,0,n,maze,visited,ans,"")
   
print(ans)
    

