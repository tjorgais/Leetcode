class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #********Time complexity O(nlogn)(sorting + iteration over the points)*********
        #Optimized Code with same approach
        if not points:
            return 0
        points.sort()
        arrow=1
        currentend=points[0][1]
        for x in points[1:]:
            if x[0]<=currentend:
                currentend=min(currentend, x[1])
            else:
                arrow+=1
                currentend=x[1]
        return arrow
        
        
        # n=len(points)
        # if n==1:
        #     return 1
        # i,j=0,1
        # points=sorted(points, key=lambda x:x[0])
        # #print(points)
        # count=0
        # while(i<n-1):
        #     x=max(points[i][0], points[j][0])
        #     y=min(points[i][1], points[j][1])
        #     if x<=y:
        #         j+=1
        #         while(j<n):
        #             if points[j][0]<=y:
        #                 x=max(x, points[j][0])
        #                 y=min(y,points[j][1])
        #             else:
        #                 count+=1
        #                 break
        #             j+=1
        #         else:
        #             count+=1
        #             break
        #         if j==n-1:
        #             count+=1
        #             break
        #         i=j
        #         j=i+1
        #     else:
        #         count+=1
        #         if j==n-1:
        #             count+=1
        #             break
        #         i=j
        #         j=i+1
        # #count=len(output)
        # #print(output)
        # return count
                
                    
                
                
        