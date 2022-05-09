class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        right=[]
        for i in range(len(nums)):
            if i==0:
                left.append(1)
            else:
                left.append(left[i-1]*nums[i-1])
        nums.reverse()
        for i in range(len(nums)):
            if i==0:
                right.append(1)
            else:
                right.append(right[i-1]*nums[i-1])
        right.reverse()
        nums.reverse()
        for i in range(len(nums)):
            nums[i]=left[i]*right[i]
        return nums


        