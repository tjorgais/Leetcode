class Solution:
    def __init__(self):
        self.max=-int(1e9+7)
    # def findmax(self, nums, count, i):
    #     n=len(nums)
    #     if i==n:
    #         return
    #     count+=nums[i]
    #     if count>self.max:
    #         self.max=count
    #     if nums[i]>self.max:
    #         self.max=nums[i]
    #     self.findmax(nums, count, i+1)
    #     self.findmax(nums, nums[i], i+1)
    #     return
            
        
        
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        count=nums[0]
        self.max=count
        for i in range(1,n):
            count=max(nums[i], count+nums[i])
            if count>self.max:
                self.max=count
        return self.max
        
        