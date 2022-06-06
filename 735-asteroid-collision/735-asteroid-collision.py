class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n=len(asteroids)
        stack=[]
        for i in range(n):      
            while(len(stack)!=0 and (asteroids[i]<0 and stack[-1]>0)):
                if abs(asteroids[i])==abs(stack[-1]):
                    stack.pop()
                    break
                elif abs(asteroids[i])>abs(stack[-1]):
                    stack.pop()
                else:
                    break
            else:
                stack.append(asteroids[i])
        return stack
                        
                       
        