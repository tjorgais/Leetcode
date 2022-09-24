from collections import Counter
from heapq import heappush, heappop
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count= Counter(nums)
        n=len(nums)
    
        return [x[0] for x in count.items() if x[1]>abs(n/3)]
#         # majority=[k for k, v in sorted(count.items(), key=lambda item: item[1]) if v>x] 
#         temp_list=[[-v, k] for k, v in count.items()]
#         heapq.heapify(temp_list)

#         nums.clear()
#         while len(temp_list)>0:
#             a,b=heappop(temp_list)
    
#             if -(a)>x:
#                 nums.append(b)
#             else:
#                 break
#         return nums