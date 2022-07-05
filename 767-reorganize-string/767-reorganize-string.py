from heapq import heappush, heappop
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        i=0
        func=Counter(s)
        if max(func.values())>(len(s)+1)/2:
            return ""
        heap=[]
        heapq.heapify(heap)
        for key in func.keys():
            heappush(heap,[-func[key],key])
        prev_freq=0
        prev_char='#'
        output=[]
        while heap:
            freq,c=heappop(heap)
            output.append(c)
            if prev_freq<0:
                heappush(heap,[prev_freq,prev_char ])
            prev_freq=freq+1
            prev_char=c
        
        return ''.join(output)