from heapq import heappush, heappop
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        n=len(nums)
        thr=int(n/2)
        max_val=-1
        max_count=-1
        for key in count.keys():
            if max_count<count[key]:
                max_count=count[key]
                max_val=key
        return max_val
            
            
        
        
        
        
            
        