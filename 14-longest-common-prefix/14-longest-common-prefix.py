class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        

        match=strs[0]
        
        
        for i in range(1,n):
            x=strs[i]
            m=len(x)
            j=1
            if m<len(match):
                
                while(j!=m+1):
                    if match[:j]!=x[:j]:
                        match=match[:j-1]
                        break
                    
                        
                    j+=1
                if j==m+1:
                    match=x[:m]
                
            else:
                while(j!=len(match)+1):
                    if match[:j]!=x[:j]:
                        match=match[:j-1]
                        break
                    j+=1
        return match
                    
                        
        