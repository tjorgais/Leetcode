from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return 0
        n=len(s)
        start=0
        c=s[0]
        j=n-1
        func1=Counter(s)
        output=[]
        while(start<n):
            while j>start:
                if c==s[j]:
                    break
                j-=1
            func2=Counter(s[start:j+1])
            for key in func2:
                if func1[key]!=func2[key]:
                    c=key
                    break
                    
            else:
                output.append(len(s[start:j+1]))
                if j==n-1:
                    break
                start=j+1
                c==s[start]
                j=n-1
                continue
            j=n-1
        return output
                
                
                    
                
                
                
                
                
            
            
        