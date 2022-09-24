from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count= Counter(nums)
        n=len(nums)
        x=abs(n/3)
        majority=[k for k, v in sorted(count.items(), key=lambda item: item[1]) if v>x] 
        return majority