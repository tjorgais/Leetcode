class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack1=[]
        stack2=[]
        for i, a in enumerate(s):

            if a=='(':
                #stack1.append(a)
                stack2.append([a,i])

            if a==')':
                if len(stack2)==0:
                    stack2.append([a,i])
                else:
                    ch=stack2.pop()
                    if ch[0]!='(':
                        stack2.append(ch)
                        stack2.append([a,i])
                    else:
                        continue
        while(len(stack2)!=0):
            ch=stack2.pop()
            s = s[0 : ch[1] : ] + s[ch[1] + 1 : :]
        return s
