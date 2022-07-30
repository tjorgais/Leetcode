class Solution:

            
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        if n==1:
            return 1
        LS=[[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            LS[i][i]=1
        for ls in range(2,n+1):
            for i in range(n-ls+1):
                j=i+ls-1
                if s[i]==s[j] and ls==2:
                    LS[i][j]=2
                elif s[i]==s[j]:
                    LS[i][j]=2+LS[i+1][j-1]
                else:
                    LS[i][j]=max(LS[i+1][j], LS[i][j-1])
        return LS[0][n-1]
        
        