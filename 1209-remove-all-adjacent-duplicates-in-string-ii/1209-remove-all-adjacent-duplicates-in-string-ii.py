class Solution:
    # def check_previous(self, stack):
    #     if not stack:
    #         return 0
    #     count=1
    #     i=-1
    #     temp=[]
    #     x=stack.pop()
    #     temp.append(x)
    #     while(stack and stack[-1]==x ):
    #         temp.append(stack.pop())
    #         count+=1
    #     while(temp):
    #         stack.append(temp.pop())
    #     return count

    
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        n=len(s)
        count=0
        i=0

        while(i!=n):


            if not stack or stack[-1][0]!=s[i]:
                stack.append([s[i],1])
            else:
                x,y=stack.pop()
                stack.append([x,y+1])
                if stack[-1][1]==k:
                    stack.pop()
            i+=1
        output=[]
        print(stack)
        while(stack):
            x,y=stack.pop()
            while(y):
                output.append(x)
                y-=1
        
            
        return "".join(output[::-1])
        