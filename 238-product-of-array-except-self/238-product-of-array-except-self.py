class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        right=1
        n=len(nums)
        for i in range(len(nums)):
            if i==0:
                left.append(1)
            else:
                left.append(left[i-1]*nums[i-1])
        
        for i in range(len(nums)):
            left[n-i-1]=left[n-i-1]*right
            right*=nums[n-i-1]
        return left
            




        