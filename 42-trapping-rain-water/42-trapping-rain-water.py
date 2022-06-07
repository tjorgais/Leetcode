class Solution:
    def trap(self, height: List[int]) -> int:
        #******Two Pointer Approach*********
        '''
        n=len(height)
        left_max=0
        right_max=0
        left=0
        right=n-1
        result=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=left_max:
                    max_left=height[left]
                else:
                    result+=(left_max-height[left])
                left+=1
            else:
                if height[right]>=right_max:
                    right_max=height[right]
                else:
                    result+=(right_max-height[right])
                right-=1
        return result
        '''
                    
                    
        ###************Stack Method************
        
        n= len(height)
        stack=[]
        result=0
        for current in range(n):
            while(stack and height[current]>height[stack[-1]]):
                prev=stack.pop()
                if not stack:
                    break
                result+=(current-stack[-1]-1)*(min(height[current],height[stack[-1]])-height[prev])
            stack.append(current)
        return result
        
            
            
        
        ###*******Order of N space method(DP)****
        '''
        n=len(height)
        left_max=[]
        right_max=[]
        maxim=-1
        for i in range(n):
            maxim=max(height[i],maxim)
            left_max.append(maxim)
        maxim=-1
        
        for i in range(n-1,-1,-1):
            maxim=max(height[i],maxim)
            right_max.append(maxim)
        right_max.reverse()

        count=0
        for i in range(n):
            x=min(left_max[i],right_max[i])
            count+=(x-height[i])
        return count
        '''    
        