
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        n=len(board)
        m=len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j]==0:
                    board[i][j]=2
        matrix=[[board[i][j] for j in range(m)]for i in range(n)]
        neighbors=[(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]
        for i in range(n):
            for j in range(m):
                count=0
                for neighbor in neighbors:
                    r=i+neighbor[0]
                    c=j+neighbor[1]

                    if (r>=0 and r<n) and (c>=0 and c<m) and abs(matrix[r][c])==1:
                        count+=1
                if matrix[i][j]==1 and (count<2 or count>3):
                    board[i][j]=-1
                if abs(matrix[i][j])==2 and (count==3):
                    board[i][j]=-2
        for i in range(n):
            for j in range(m):
                if board[i][j]==-1:
                    board[i][j]=0
                elif board[i][j]==2:
                    board[i][j]=0
                elif board[i][j]==-2:
                    board[i][j]=1

        return 