class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        val=sum(nums)
        
        if  (val+target)%2!=0 or val<target:
            return 0
        if len(nums) == 1:
            if abs(nums[0]) != abs(target):
                return 0
            else:
                return 1
        val_tot=(val+target)//2
        ts=[[ 0 for j in range(val_tot+1)] for i in range(n+1)]
        #print(ts)
        for j in range(val_tot+1):
            ts[0][j]=0
        for i in range(n+1):
            ts[i][0]=1
        for i in range(1, n+1):
            for j in range( val_tot+1):
                if j>=nums[i-1]:
                    ts[i][j]=ts[i-1][j]+ts[i-1][j-nums[i-1]]
                else:
                    ts[i][j]=ts[i-1][j]
                    
        
        return ts[n][val_tot]
                    
                
            
            
        