class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff=20000
        prev_diff=20000
        final_sum=0


        for i in range(n - 2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while (j < k):

                x=nums[i]+nums[j]+nums[k]
                diff=abs(x-target)
                
                if diff==0:
                    final_sum=x
                    return final_sum
                if diff < prev_diff:
                    final_sum = x
                    prev_diff = diff

                if x > target:
                    k -= 1
                elif x < target:
                    j += 1


        return final_sum
        