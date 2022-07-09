class Solution:
    def check_previous(self, stack):
        if not stack:
            return 0
        count=1
        i=-1
        temp=[]
        x=stack.pop()
        temp.append(x)
        while(stack and stack[-1]==x ):
            temp.append(stack.pop())
            count+=1
        while(temp):
            stack.append(temp.pop())
        return count
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        n=len(s)
        count=0
        i=0

        while(i!=n):

            if not stack:
                stack.append(s[i])
                count=1
                i+=1
                continue
            x=stack[-1]
            if x!=s[i]:
                stack.append(s[i])
                count=1
            else:


                if count==k-1:
                    j=0
                    removed=True
                    while(j!=k-1):
                        stack.pop()
                        j+=1
                    count=self.check_previous(stack)

                else:
                    stack.append(s[i])
                    count+=1
            i+=1
                
        return "".join(stack)
        