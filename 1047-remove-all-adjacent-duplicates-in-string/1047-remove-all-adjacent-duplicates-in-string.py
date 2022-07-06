class Solution:
    def removeDuplicates(self, s: str) -> str:
        n=len(s)
        stack=[]
        i=1
        stack.append(s[0])
        while(True):
            x=stack.pop()
            if x!=s[i]:
                stack.append(x)
                stack.append(s[i])
            else:
                if not stack:
                    i+=1
                    if i!=n:
                        stack.append(s[i])
                    else:
                        break
            i+=1
            if i==n:
                break
        return "".join(stack)
                    
                    
                    
            