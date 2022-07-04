from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        n=len(nums)
        freq = {}
        for i in range(n):
            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1
        heap=[]
        heapq.heapify(heap)
        for key in freq.keys():
            heappush(heap,[-freq[key],key])
        #print(heap)
        output=[]
        while(k):
            x,y=heappop(heap)
            output.append(y)
            k-=1
        return output
        
        
        
#         n=len(nums)
#         freq = {}
#         for i in range(n):
#             if nums[i] in freq:
#                 freq[nums[i]] += 1
#             else:
#                 freq[nums[i]] = 1
#         a=[0]*(len(freq))
#         print(a)
#         j=0
#         for keys in freq:

#             a[j]=[keys, freq[keys]]
#             j+=1
#         a = sorted(a, key=lambda x: x[1], reverse=True)

#         return [a[i][0] for i in range(k)]