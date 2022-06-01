class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            print(i)
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            if len(stack)==0:
                return False
            if i==')':
                ch=stack.pop()
                if ch!='(':
                    return False
            if i=='}':
                ch=stack.pop()
                if ch!='{':
                    return False
            if i==']':
                ch=stack.pop()
                if ch!='[':
                    return False
        if len(stack)!=0:
            return False
        else:
            return True
            
                    
        