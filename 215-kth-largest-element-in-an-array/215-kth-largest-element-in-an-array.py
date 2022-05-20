from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        heapmax=[]
        heapmin=[]
        for i in range(n):
            if len(heapmax) == 0:
                heappush(heapmax, -nums[i])
            elif len(heapmax) <n-k+1 :
                heappush(heapmax, -nums[i])
                # ele = heappop(heapmax)
                # heappush(heapmin, -ele)
            elif len(heapmax) == n-k+1:
                heappush(heapmax, -nums[i])
                ele = heappop(heapmax)
                heappush(heapmin, -ele)

        return -heapmax[0]
        