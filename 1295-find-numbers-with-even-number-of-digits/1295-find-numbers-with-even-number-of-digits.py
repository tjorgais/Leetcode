class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        for i in range(n):
            digits=0
            x=nums[i]
            while(x):
                x=x//10
                digits+=1
            if digits%2==0:
                count+=1
        return count



