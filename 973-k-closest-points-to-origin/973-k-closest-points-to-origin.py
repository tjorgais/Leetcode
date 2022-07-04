from heapq import heappush, heappop
import numpy as np
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n=len(points)
        func=[]
        i=0
        heapq.heapify(func)
        for point in points:
            x=np.square(point[0])+np.square(point[1])
            func.append([x, point])
        func.sort()
        output=[]
        while(k):
            x,y=heappop(func)
            output.append(y)
            k-=1
        return output
            
        
            
        
#         while(k!=0):
            
#             k-=1