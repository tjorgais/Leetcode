class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n=len(points)
        if n==1:
            return 1
        i,j=0,1
        points=sorted(points, key=lambda x:x[0])
        #print(points)
        output=[]
        while(i<n-1):
            x=max(points[i][0], points[j][0])
            y=min(points[i][1], points[j][1])
            if x<=y:
                j+=1
                while(j<n):
                    if points[j][0]<=y:
                        x=max(x, points[j][0])
                        y=min(y,points[j][1])
                    else:
                        output.append([x,y])
                        break
                    j+=1
                else:
                    output.append([x,y])
                    break
                if j==n-1:
                    output.append([points[j][0],points[j][1]])
                    break
                i=j
                j=i+1
            else:
                output.append([points[i][0],points[i][1]])
                if j==n-1:
                    output.append([points[j][0],points[j][1]])
                    break
                i=j
                j=i+1
        count=len(output)
        #print(output)
        return count
                
                    
                
                
        