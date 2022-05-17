class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        my_list = []

        for i in range(n - 3):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for l in range(n-1, i+2,-1):
                if l<n-1 and nums[l]==nums[l+1]:
                    continue
                j = i + 1
                k = l - 1
                while (j < k):
                    x = nums[i] + nums[j] + nums[k]+nums[l]

                    if x > target:
                        k = k - 1
                    elif x < target:
                        j = j + 1
                    else:
                        my_list.append((nums[i], nums[j], nums[k], nums[l]))

                        k = k - 1
                        while j < k and nums[k] == nums[k + 1]:
                            k = k - 1

        return my_list
        