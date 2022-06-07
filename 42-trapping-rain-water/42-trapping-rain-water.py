class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left_max=[]
        right_max=[]
        maxim=-1
        for i in range(n):
            maxim=max(height[i],maxim)
            left_max.append(maxim)
        maxim=-1
        
        for i in range(n-1,-1,-1):
            maxim=max(height[i],maxim)
            right_max.append(maxim)
        right_max.reverse()

        count=0
        for i in range(n):
            x=min(left_max[i],right_max[i])
            count+=(x-height[i])
        return count
            
        