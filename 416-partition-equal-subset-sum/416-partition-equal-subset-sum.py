class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #Solve by 0/1 knapsack problem
        
        val=sum(nums)
        if (val & 1) ==1:
            return False
        val//=2
        n=len(nums)
        dp=[[False for j in range(val+1)] for i in range(n+1)]
        dp[0][0]=True
        for i in range(1,n+1):
            dp[i][0]=True
        for j in range(1,val+1):
            dp[0][j]=False

        for i in range(1, n+1):
            for j in range(1, val+1):
                dp[i][j]=dp[i-1][j]
                if j>=nums[i-1]:
                    dp[i][j]=dp[i][j] or dp[i-1][j-nums[i-1]]
        return dp[n][val]
        

            
            
            
            