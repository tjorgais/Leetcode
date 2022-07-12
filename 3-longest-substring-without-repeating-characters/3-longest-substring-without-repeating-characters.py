from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        ans=0
        i=0
        j=0
        func={}
        while(j<n):
            if s[j] in func:
                func[s[j]]+=1
            else:
                func[s[j]]=1
            while(func[s[j]]>1):
                func[s[i]]-=1
                i+=1
            ans=max(ans,j-i+1)
            j+=1
        return ans
            
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n=len(s)
#         if n==0:
#             return 0
#         odd=n
#         for i in range(n-1,-1,-1):
#             j=0
#             k=i+1
#             func={}
#             while(k!=n+1):
#                 func=Counter(s[j:k])
                
#                 for key in func.keys():
                    
#                     if func[key]!=1:
#                         break
#                 else:
#                     odd=i+1
#                     break
#                 j+=1
#                 k+=1
#                 continue
#             else:
#                 continue
#             break
#         return odd
                    
                        
                    
                        
                
                
            
        