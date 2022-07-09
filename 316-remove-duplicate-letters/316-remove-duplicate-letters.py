class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n=len(s)
        last=[0]*26
        for i in range(n):
            last[ord(s[i])-97]=i
        seen=[False]*26
        stack=[]
        for i in range(n):
            x=ord(s[i])-97
            if seen[x]:
                continue
            while(stack and stack[-1]>s[i] and i< last[ord(stack[-1])-97]):
                seen[ord(stack[-1])-97]=False
                stack.pop()
            stack.append(s[i])
            seen[x]=True
        return ''.join(stack)
        