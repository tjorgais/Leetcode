class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        col=False
        for i in range( m):
            for j in range( n):
                if matrix[i][j]==0:
                    if i!=0 and j==0:
                        col=True
                    elif i==0 and j!=0:
                        matrix[0][0]=0
                    elif i==0 and j==0:
                        matrix[0][0]=0
                        col=True
                    else:
                        matrix[i][0]=0
                        matrix[0][j]=0
        print(matrix)
        print(col)

        i=1
        k=1
        while i<m:

            if matrix[i][0]==0:
                for j in range(n):

                    matrix[i][j]=0
            i=i+1
        while k<n:
            if matrix[0][k]==0:
                for j in range(m):
                    matrix[j][k]=0
            k=k+1

        if matrix[0][0] == 0 and col == True:
            for j in range(m):
                matrix[j][0] = 0
            for j in range(n):
                matrix[0][j] = 0

        if matrix[0][0]==0 and col==False:
            for j in range(n):
                matrix[0][j] = 0

        if matrix[0][0] != 0 and col == True:
            for j in range(m):
                matrix[j][0] = 0

        return matrix
        