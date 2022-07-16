from heapq import heappush, heappop
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        n=len(s)
        a=[]
        for count, c in sorted((s.count(c),c) for c in set(s)):
            if count>(n+1)/2:
                return ""
            a.extend(c*count)
        result=[None]*n
        result[::2]=a[n//2:]
        result[1::2]=a[:n//2]
        return ''.join(result)
        
            
            
        #Using heap
#         i=0
#         func=Counter(s)
#         if max(func.values())>(len(s)+1)/2:
#             return ""
#         heap=[]
#         heapq.heapify(he    ap)
#         for key in func.keys():
#             heappush(heap,[-func[key],key])
#         prev_freq=0
#         prev_char='#'
#         output=[]
#         while heap:
#             freq,c=heappop(heap)
#             output.append(c)
#             if prev_freq<0:
#                 heappush(heap,[prev_freq,prev_char ])
#             prev_freq=freq+1
#             prev_char=c
        
#         return ''.join(output)