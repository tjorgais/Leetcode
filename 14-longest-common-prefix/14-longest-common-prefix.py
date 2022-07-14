class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        n=len(strs)
        minlen=len(strs[0])
        for i in range(1,n):
            if len(strs[i])<minlen:
                minlen=len(strs[i])
        output=''
        for i in range(minlen):
            curr=strs[0][i]
            for j in range(1,n):
                if strs[j][i]!=curr:
                    return output
            output+=curr
        return output
                    
                
        
        
        
        #Time complexity of O(N*L) where L is length of the string in worse case
#         n=len(strs) 
#         match=strs[0]
#         for i in range(1,n):
#             x=strs[i]
#             m=len(x)
#             j=1
#             if m<len(match):
                
#                 while(j!=m+1):
#                     if match[:j]!=x[:j]:
#                         match=match[:j-1]
#                         break
                    
                        
#                     j+=1
#                 if j==m+1:
#                     match=x[:m]
                
#             else:
#                 while(j!=len(match)+1):
#                     if match[:j]!=x[:j]:
#                         match=match[:j-1]
#                         break
#                     j+=1
#         return match
                    
                        
        