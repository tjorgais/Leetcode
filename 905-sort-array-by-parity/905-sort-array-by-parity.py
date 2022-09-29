class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        arr1=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                arr1.insert(0,nums[i])
            else:
                arr1.append(nums[i])
        return arr1
        