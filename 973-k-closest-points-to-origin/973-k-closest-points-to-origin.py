from heapq import heappush, heappop
import numpy as np
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n=len(points)
        func=[]
        i=0
        heapq.heapify(func)
        for point in points:
            x=np.linalg.norm(point)
            func.append([x, point])
        func.sort()
        points.clear()
        while(k):
            x,y=heappop(func)
            points.append(y)
            k-=1
        return points
            
        
            
        
#         while(k!=0):
            
#             k-=1