class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        slow=nums[0]
        fast=nums[nums[0]]
        while(fast!=slow):
            slow=nums[slow]
            
            fast=nums[nums[fast]]
        fast = 0;
        while (fast != slow):
            
            fast = nums[fast];
            slow = nums[slow];
        
        return slow
            
        
        