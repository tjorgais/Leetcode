class Solution:
    def isPalindrome(self, s):
 
    

        l = len(s)

        
        if l < 2:
            return True

        # If s[0] and s[l-1] are equal
        elif s[0] == s[l - 1]:

            # Call is palindrome form substring(1,l-1)
            return self.isPalindrome(s[1: l - 1])

        else:
            return False
    def count_palindrome(self, s, LS, n):
        
        for i in range(n):
            LS[i][i]=[1,1]
        for ls in range(2, n+1):
            for i in range(n-ls+1):
                j=i+ls-1
                if ls==2:
                    #print(i,j)
                    if s[i]!=s[j]:
                        LS[i][j]=[2,0]
                    else:
                        LS[i][j]=[3,1]
                else:
                    if s[i]==s[j] and LS[i+1][j-1][1]==1:
                        LS[i][j]=[-LS[i+1][j-1][0]+LS[i][j-1][0]+LS[i+1][j][0]+1,1]
                    else:
                        LS[i][j]=[-LS[i+1][j-1][0]+LS[i][j-1][0]+LS[i+1][j][0],0]
        #print(LS)
        return LS[0][n-1][0]
        
    def countSubstrings(self, s: str) -> int:
        
        n=len(s)
        LS=[[[0,0] for j in range(n)] for i in range(n)]  #each window contain two entries first one is count of palindrome and second one is if the LS[i+1][j-1] is palindrome or not
        return self.count_palindrome(s, LS, n)

                
            
        
        
        