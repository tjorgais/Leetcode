maxint=int(1e9+7)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)
        nums.append(1)
        n=len(nums)
        mat=[[0 for i in range(n)] for j in range(n)]
        for l in range(2,n):
            for i in range(1, n-l+1):
                j=i+l-1
                mat[i][j]=-maxint
                for k in range(i,j):
                    x=mat[i][k]+mat[k+1][j]+nums[i-1]*nums[k]*nums[j]
                    if x>mat[i][j]:
                        mat[i][j]=x
        #print(mat)
        return mat[1][n-1]
        
        