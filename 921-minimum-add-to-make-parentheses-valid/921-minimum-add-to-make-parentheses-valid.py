class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n=len(s)
        left=0
        right=0
        imbalance=0
        stack=[]
        
        for i in range(n):
            if not stack and s[i]==')':
                imbalance+=1
            elif not stack and s[i]=='(':
                stack.append('(')
            else:
                c=stack[-1]
                if s[i]!=')':
                    stack.append('(')
                else:
                    stack.pop()
        return imbalance + len(stack)
            
                
            
         
        return imbalance
            