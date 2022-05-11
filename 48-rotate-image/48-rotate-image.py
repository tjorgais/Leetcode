class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n=len(matrix)
        s=n
        x=(int)(n//2)
        for i in range(0,x):
            for j in range(i, n-i-1):
                temp1=matrix[i][j]
                temp3=matrix[n-i-1][n-j-1]
                
                matrix[i][j]=matrix[n-j-1][i]
                
                matrix[n-i-1][n-j-1]=matrix[j][n-i-1]
                matrix[j][n-i-1]=temp1
                matrix[n-j-1][i]=temp3


        return matrix
        