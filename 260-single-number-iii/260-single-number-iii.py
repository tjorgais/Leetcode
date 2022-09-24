from collections import Counter 
from heapq import heappush, heappop
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        arr=[[v, k] for k,v in count.items()]
        heapq.heapify(arr)
        nums.clear()
        for i in range(2):
            a,b=heappop(arr)
            if a==1:
                nums.append(b)
        return nums
                
        