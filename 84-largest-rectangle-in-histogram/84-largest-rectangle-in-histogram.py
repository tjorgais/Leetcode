class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        i=0
        stack=[]
        maxarea=0
        while(i<n):
            if (not stack) or (heights[i]>= heights[stack[-1]]):
                stack.append(i)
                i+=1
            else:
                topele=stack.pop()
                area=heights[topele]*((i-stack[-1]-1)if stack else i)
                maxarea=max(area, maxarea)
        while(stack):
            topele=stack.pop()
            area=heights[topele]*((i-stack[-1]-1)if stack else i)
            maxarea=max(area, maxarea)
        return maxarea
            
                
        