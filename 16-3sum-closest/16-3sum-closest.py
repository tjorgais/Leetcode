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
                diff=x-target
                abs_diff=abs(diff)
                if abs_diff==0:
                    final_sum=x
                    return final_sum
                elif abs_diff<prev_diff:
                    final_sum=x
                    prev_diff=abs_diff
                    if target>=0 and x<0:
                        j+=1
                    elif target<0 and x>=0:
                        k-=1
                    else:
                        if diff>0:
                            k-=1
                        else:
                            j+=1
                else:
                    if target >= 0 and x < 0:
                        j += 1
                    elif target < 0 and x >= 0:
                        k -= 1
                    else:
                        if diff > 0:
                            k -= 1
                        else:
                            j += 1



        return final_sum
        